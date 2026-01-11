# Azure Copilot Migrate - Modernized ASP.NET Core Application

A modernized ASP.NET Core web application optimized for Azure deployment with best practices.

## Features

- ✅ **Modern ASP.NET Core 8.0** with top-level statements
- ✅ **Structured Logging** with console, debug, and event source providers
- ✅ **Application Insights** integration for Azure monitoring
- ✅ **Health Checks** with detailed endpoints (`/health`, `/health/ready`, `/health/live`)
- ✅ **OpenAPI/Swagger** documentation (available in development mode)
- ✅ **Security Headers** (X-Content-Type-Options, X-Frame-Options, CSP, etc.)
- ✅ **CORS Support** configured for cross-origin requests
- ✅ **Azure-friendly PORT binding** for App Service and containers
- ✅ **Razor Pages** support
- ✅ **RESTful API endpoints** with OpenAPI annotations

## Prerequisites

- .NET 8.0 SDK or later
- Visual Studio 2022, VS Code, or any .NET-compatible IDE

## Getting Started

### Restore dependencies
```bash
dotnet restore
```

### Run locally
```bash
dotnet run
```

The application will start on `http://localhost:8080` by default.

### Build
```bash
dotnet build
```

### Publish
```bash
dotnet publish -c Release -o ./publish
```

## Endpoints

- **`/`** - Main Razor Pages application
- **`/health`** - Detailed health check with JSON response
- **`/health/ready`** - Readiness probe (for Kubernetes/container orchestrators)
- **`/health/live`** - Liveness probe
- **`/api/info`** - Application information endpoint
- **`/swagger`** - OpenAPI documentation (development only)

## Azure Deployment

### Application Insights Configuration

Set the connection string via environment variable:
```bash
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=xxx;IngestionEndpoint=https://...
```

Or configure in `appsettings.json`:
```json
{
  "ApplicationInsights": {
    "ConnectionString": "your-connection-string"
  }
}
```

### Deploy to Azure App Service

```bash
az webapp up --name your-app-name --resource-group your-rg --runtime "DOTNET|8.0"
```

### Deploy with Azure Container Apps

```bash
az containerapp up --name your-app --resource-group your-rg --source .
```

## Configuration

Configure the application through:
- `appsettings.json` - Base configuration
- `appsettings.Development.json` - Development overrides
- Environment variables
- Azure App Configuration (if integrated)

## Security Features

The application includes production security headers:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `Referrer-Policy: no-referrer`
- `Content-Security-Policy: default-src 'self'`

## Logging

Structured logging is configured with:
- Console output for Azure App Service
- Debug output for development
- Event Source for performance monitoring
- Application Insights integration (when configured)

## License

MIT