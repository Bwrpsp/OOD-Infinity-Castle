# Infinity Castle

Hilbert Infinite Hotel Project - Muzan's Infinity Castle with Room Management

## Features

### Core Functionality
- 🏰 **Room Management**: Add, remove, and search for demons in castle rooms
- 🔢 **Multiple Adding Methods**: Support for various infinite demon addition strategies
- 🌲 **AVL Tree Structure**: Efficient self-balancing tree for O(log n) operations
- 📊 **Data Export/Import**: Save and load castle configurations via CSV

### New Features
- 💾 **Castle CSV Export** (Option 5): Export all rooms and demons to CSV file
- 📥 **Castle CSV Import** (Option 6): Import castle data from CSV file
- ⚡ **Performance Tracking** (Options 7-8): Track RAM usage and execution time
- 📈 **Performance Metrics Export**: Export performance statistics to CSV

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirement.txt
```

### 2. Run the Application

```bash
python main.py
```

### 3. Available Commands

| Command | Description |
|---------|-------------|
| 1 | Show all demons in castle |
| 2 | Add demon(s) using various methods |
| 3 | Remove demon from a room |
| 4 | Search for demon by room number |
| 5 | Export castle data to CSV |
| 6 | Import castle data from CSV |
| 7 | Export performance metrics to CSV |
| 8 | View performance summary |
| Help | Show help menu |
| Quit | Exit program (option to export before exit) |

## Demon Adding Methods

### Method 1: Add n Demons
Add a specific number of demons to consecutive rooms.

### Method 2: Add Infinite Demons
Add infinite demons using the doubling technique (odd numbers).

### Method 3: Add Infinite Demons on n Buses
Distribute infinite demons across multiple buses.

### Method 4: Add Infinite Demons on Infinite Buses
The ultimate challenge - infinite demons on infinite buses!

### Method 5: Manual Addition
Manually assign a demon to a specific room number.

## Data Export/Import

### Export Castle Data
```
1. Select option 5
2. File auto-saved as: castle_data_YYYYMMDD_HHMMSS.csv
3. Contains all room numbers and demon IDs
```

### Import Castle Data
```
1. Select option 6
2. Enter CSV filename
3. Rooms are added to current castle
```

**CSV Format:**
```csv
room_number,demon_id
1,OG-L0-D1
2,OG-L0-D2
3,OG-L0-D3
```

See [CASTLE_EXPORT_GUIDE.md](CASTLE_EXPORT_GUIDE.md) for detailed documentation.

## Performance Tracking

Track execution time and RAM usage for every operation:
- Real-time performance display after each command
- Export metrics to CSV for analysis
- View summary statistics

See [PERFORMANCE_TRACKING.md](PERFORMANCE_TRACKING.md) for detailed documentation.

## Documentation

- 📘 [Castle Export Guide](CASTLE_EXPORT_GUIDE.md) - Complete guide to CSV export/import
- 📊 [Performance Tracking](PERFORMANCE_TRACKING.md) - Performance monitoring documentation
- 🚀 [Quick Start Guide](QUICKSTART.md) - Get started quickly
- 📋 [Implementation Summary](IMPLEMENTATION_SUMMARY.md) - Technical implementation details

## Project Structure

```
OOD-Infinity-Castle/
├── main.py                 # Main application entry point
├── AvlTree.py             # AVL tree implementation for room management
├── room.py                # Room class and utilities
├── demon.py               # Demon ID generation
├── castle_export.py       # CSV export/import functionality
├── performance_tracker.py # Performance monitoring
├── ascii.py               # ASCII art and UI utilities
├── primegen.py            # Prime number generation utilities
└── requirement.txt        # Python dependencies
```

## Requirements

- Python 3.7+
- tqdm (progress bars)
- psutil (performance monitoring)

## License

Educational project for Object-Oriented Design course.
