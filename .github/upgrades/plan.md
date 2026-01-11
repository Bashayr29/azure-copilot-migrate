# .NET 9.0 Upgrade Plan

## Execution Steps

Execute steps below sequentially one by one in the order they are listed.

1. Validate that a .NET 9.0 SDK required for this upgrade is installed on the machine and if not, help to get it installed.
2. Ensure that the SDK version specified in global.json files is compatible with the .NET 9.0 upgrade.
3. Upgrade azure-copilot-migrate.csproj to .NET 9.0

## Settings

This section contains settings and data used by execution steps.

### Aggregate NuGet packages modifications across all projects

NuGet packages used across all selected projects or their dependencies that need version update in projects that reference them.

| Package Name                                    | Current Version | New Version | Description                                   |
|:------------------------------------------------|:---------------:|:-----------:|:----------------------------------------------|
| Microsoft.ApplicationInsights.AspNetCore        |   2.22.0        |  2.22.0+    | Recommended for .NET 9.0                      |
| Microsoft.AspNetCore.OpenApi                    |   8.0.0         |  9.0.0      | Recommended for .NET 9.0                      |
| Microsoft.Extensions.Diagnostics.HealthChecks   |   8.0.0         |  9.0.0      | Recommended for .NET 9.0                      |
| Swashbuckle.AspNetCore                          |   6.5.0         |  6.5.0+     | Recommended for .NET 9.0                      |

### Project upgrade details

This section contains details about each project upgrade and modifications that need to be done in the project.

#### azure-copilot-migrate.csproj modifications

Project properties changes:
  - Target framework should be changed from `net8.0` to `net9.0`

NuGet packages changes:
  - Microsoft.ApplicationInsights.AspNetCore should be updated from `2.22.0` to latest compatible version (*recommended for .NET 9.0*)
  - Microsoft.AspNetCore.OpenApi should be updated from `8.0.0` to `9.0.0` (*recommended for .NET 9.0*)
  - Microsoft.Extensions.Diagnostics.HealthChecks should be updated from `8.0.0` to `9.0.0` (*recommended for .NET 9.0*)
  - Swashbuckle.AspNetCore should be updated from `6.5.0` to latest compatible version (*recommended for .NET 9.0*)
