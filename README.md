# Delivery Route Planner

A command-line application that simulates a day of package deliveries for the
fictional Western Governors University Parcel Service (WGUPS). It routes three
trucks through 40 packages, then lets you check the status of any package, or
all packages, at any time of day.

## Features

- Routes 40 packages across 3 trucks using a **nearest neighbor** algorithm
- Custom **hash map** (separate chaining) for package storage and lookup, with no built-in `dict`
- Handles special package constraints: delayed arrivals, truck-specific
  packages, deadlines, and a package with a wrong address that is corrected at 10:20 AM
- Status lookup at any time: `at hub`, `en route`, or `delivered`, with the delivery time
- Per-truck and total mileage reporting

## Requirements

- Python 3.10 or newer (standard library only, no external dependencies)

## Running

Run from the project directory, since the CSV files are read using relative paths:

```
python main.py
```

Menu options:

1. **View all packages at a specific time frame**: enter a time and see every
   package's status at that moment, plus truck mileage
2. **Look up a single package**: enter a time and a package ID (1-40)
3. **Exit**

Times are entered as `hour:min AM/PM`, for example `9:15 AM` or `1:30 PM`.

## Project Structure

| File | Purpose |
| --- | --- |
| `main.py` | Entry point; creates the service and launches the UI |
| `DeliveryRoutingService.py` | Routing logic: loads packages and trucks, runs nearest neighbor, simulates the day up to a query time |
| `WGUPSUserInterface.py` | Command-line menu, input validation, and output |
| `Truck.py` | Truck state: loaded packages, location, clock, and mileage (18 mph) |
| `Package.py` | Package data and status/delivery details |
| `HashMap.py` | Custom hash table with fixed-size buckets |
| `DistanceTable.py` | Loads the distance CSV and returns the distance between two addresses |
| `Color.py` | Terminal color codes for output |
| `WGUPS Package File.csv` | Package data (address, deadline, weight, notes) |
| `WGUPS Distance Table.csv` | Distances in miles between all delivery locations |

## How It Works

Each query re-runs the simulation from the start of the day up to the requested
time, so results always reflect that moment.

1. Packages are loaded from CSV into the hash map, all starting as `at hub`.
2. **Truck 2** departs at 8:00 AM with truck-2-only and early-deadline packages.
3. **Truck 1** departs at 9:05 AM with the packages delayed on a flight.
4. **Truck 3** departs once truck 2 finishes and returns to the hub, since only
   two drivers are available. It carries the remaining packages, including
   package 9 after its address is corrected at 10:20 AM.
5. Each truck repeatedly drives to the nearest remaining delivery. Time is
   computed from distance at 18 mph, and the simulation stops when the clock
   reaches the query time.

## Complexity

- Hash map `put` / `get`: O(1) average
- Nearest neighbor routing per truck: O(n²) in the number of packages on the truck
- Package loading from CSV: O(n)

