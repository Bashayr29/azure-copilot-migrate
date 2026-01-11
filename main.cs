using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Diagnostics.HealthChecks;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Diagnostics.HealthChecks;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);

// Configure logging
builder.Logging.ClearProviders();
builder.Logging.AddConsole();
builder.Logging.AddDebug();
builder.Logging.AddEventSourceLogger();

// Add Application Insights telemetry if configured
if (!string.IsNullOrEmpty(builder.Configuration["APPLICATIONINSIGHTS_CONNECTION_STRING"]))
{
    builder.Services.AddApplicationInsightsTelemetry();
}

// Add services
builder.Services.AddRazorPages();

// Add health checks
builder.Services.AddHealthChecks()
    .AddCheck("self", () => HealthCheckResult.Healthy("Application is running"))
    .AddCheck("ready", () => HealthCheckResult.Healthy("Application is ready"));

// Add CORS if needed
builder.Services.AddCors(options =>
{
    options.AddPolicy("DefaultPolicy", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

// Add API documentation
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new() { 
        Title = "Azure Copilot Migrate API", 
        Version = "v1",
        Description = "Modernized ASP.NET Core application for Azure deployment"
    });
});

var app = builder.Build();

var logger = app.Logger;

// Azure-friendly binding helper
// - Azure App Service (Linux / containers) may inject PORT
// - Safe for Windows App Service and local runs
var portEnv = Environment.GetEnvironmentVariable("PORT");
if (int.TryParse(portEnv, out var port))
{
    app.Urls.Add($"http://*:{port}");
    logger.LogInformation("Binding to port {Port} from environment", port);
}
else
{
    // Local predictable port
    app.Urls.Add("http://*:8080");
    logger.LogInformation("Binding to default port 8080");
}

// Middleware pipeline
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "API v1"));
    app.UseDeveloperExceptionPage();
}
else
{
    app.UseExceptionHandler("/Error");
    // Add security headers
    app.Use(async (context, next) =>
    {
        context.Response.Headers.Append("X-Content-Type-Options", "nosniff");
        context.Response.Headers.Append("X-Frame-Options", "DENY");
        context.Response.Headers.Append("X-XSS-Protection", "1; mode=block");
        context.Response.Headers.Append("Referrer-Policy", "no-referrer");
        context.Response.Headers.Append("Content-Security-Policy", "default-src 'self'");
        await next();
    });
}

app.UseStaticFiles();
app.UseRouting();
app.UseCors("DefaultPolicy");

// Health check endpoints for Azure App Service and container orchestrators
app.MapHealthChecks("/health", new HealthCheckOptions
{
    ResponseWriter = async (context, report) =>
    {
        context.Response.ContentType = "application/json";
        var result = JsonSerializer.Serialize(new
        {
            status = report.Status.ToString(),
            checks = report.Entries.Select(e => new
            {
                name = e.Key,
                status = e.Value.Status.ToString(),
                description = e.Value.Description,
                duration = e.Value.Duration.ToString()
            }),
            totalDuration = report.TotalDuration.ToString()
        });
        await context.Response.WriteAsync(result);
    }
});

app.MapHealthChecks("/health/ready", new HealthCheckOptions
{
    Predicate = check => check.Tags.Contains("ready") || check.Name == "ready"
});

app.MapHealthChecks("/health/live", new HealthCheckOptions
{
    Predicate = _ => false
});

// API endpoints
app.MapGet("/api/info", (IHostEnvironment env) =>
{
    logger.LogInformation("Info endpoint called");
    return Results.Ok(new
    {
        application = "Azure Copilot Migrate",
        environment = env.EnvironmentName,
        version = "1.0.0",
        timestamp = DateTime.UtcNow,
        machineName = Environment.MachineName
    });
}).WithName("GetInfo")
  .WithOpenApi();

app.MapRazorPages();

logger.LogInformation("Application starting in {Environment} environment", app.Environment.EnvironmentName);

app.Run();