using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
 
var builder = WebApplication.CreateBuilder(args);
 
// Add Razor Pages services
builder.Services.AddRazorPages();
 
var app = builder.Build();
 
// Azure-friendly binding helper
// - Azure App Service (Linux / containers) may inject PORT
// - Safe for Windows App Service and local runs
var portEnv = Environment.GetEnvironmentVariable("PORT");
if (int.TryParse(portEnv, out var port))
{
    app.Urls.Add($"http://*:{port}");
}
else
{
    // Local predictable port
    app.Urls.Add("http://*:8080");
}
 
// Middleware pipeline
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
}
 
app.UseStaticFiles();
app.UseRouting();
 
// Simple health endpoint (useful for Azure probes)
app.MapGet("/health", () =>
    Results.Ok(new
    {
        status = "ok",
        environment = app.Environment.EnvironmentName,
        utc = DateTime.UtcNow
    })
);
 
app.MapRazorPages();
 
app.Run();