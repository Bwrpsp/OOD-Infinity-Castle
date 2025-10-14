"""
Test script to demonstrate castle CSV export/import functionality
"""
from AvlTree import AVLTree
from demon import generate_demon_id
from castle_export import export_castle_to_csv, import_castle_from_csv

def main():
    print("=== Castle CSV Export/Import Demo ===\n")
    
    # Create a test castle with some rooms
    print("1. Creating test castle with demons...")
    castle = AVLTree()
    
    test_rooms = [
        (1, generate_demon_id(0, 0, 1)),
        (2, generate_demon_id(0, 0, 2)),
        (3, generate_demon_id(0, 0, 3)),
        (5, generate_demon_id(0, 0, 5)),
        (8, generate_demon_id(0, 0, 8)),
        (13, generate_demon_id(0, 0, 13)),
    ]
    
    for room in test_rooms:
        castle.insertRoom(room)
    
    print(f"   ✓ Created castle with {len(test_rooms)} rooms\n")
    
    # Display all rooms
    print("2. Current castle contents:")
    print(f"   {'Room':<10} {'Demon ID':<20}")
    print("   " + "-" * 30)
    for room in castle.get_all():
        print(f"   {room.num:<10} {room.demon:<20}")
    print()
    
    # Export to CSV
    print("3. Exporting castle to CSV...")
    success, filename = export_castle_to_csv(castle, "test_castle.csv")
    
    if success:
        print(f"   ✓ Exported successfully to: {filename}\n")
    else:
        print(f"   ✗ Export failed: {filename}\n")
        return
    
    # Show CSV contents
    print("4. CSV file contents:")
    with open(filename, 'r') as f:
        print("   " + f.read().replace('\n', '\n   '))
    
    # Create new empty castle
    print("5. Creating new empty castle...")
    new_castle = AVLTree()
    print(f"   ✓ New castle created (empty)\n")
    
    # Import from CSV
    print("6. Importing data from CSV into new castle...")
    success, message, count = import_castle_from_csv(new_castle, filename)
    
    if success:
        print(f"   ✓ {message}\n")
    else:
        print(f"   ✗ {message}\n")
        return
    
    # Verify import
    print("7. Verifying imported data:")
    print(f"   {'Room':<10} {'Demon ID':<20}")
    print("   " + "-" * 30)
    for room in new_castle.get_all():
        print(f"   {room.num:<10} {room.demon:<20}")
    
    print("\n=== Demo Complete ===")
    print(f"✓ Successfully exported and imported {count} rooms")

if __name__ == "__main__":
    main()
