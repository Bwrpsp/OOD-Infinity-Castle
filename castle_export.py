import csv
from datetime import datetime

def export_castle_to_csv(castle, filename=None):
    """
    Export all rooms and demons in the castle to a CSV file
    
    Args:
        castle: AVLTree instance containing all rooms
        filename: Optional custom filename for the CSV
    
    Returns:
        tuple: (success: bool, message: str)
    """
    if filename is None:
        filename = f"castle_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        # Get all rooms from the castle
        rooms = castle.get_all()
        
        if not rooms:
            return False, "Castle is empty - no data to export"
        
        # Write to CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['room_number', 'demon_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for room in rooms:
                writer.writerow({
                    'room_number': room.num,
                    'demon_id': room.demon
                })
        
        return True, filename
    
    except Exception as e:
        return False, f"Error exporting castle data: {str(e)}"


def import_castle_from_csv(castle, filename):
    """
    Import rooms and demons from a CSV file into the castle
    
    Args:
        castle: AVLTree instance to import data into
        filename: CSV file to import from
    
    Returns:
        tuple: (success: bool, message: str, count: int)
    """
    try:
        imported_count = 0
        
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                room_number = int(row['room_number'])
                demon_id = row['demon_id']
                castle.insertRoom((room_number, demon_id))
                imported_count += 1
        
        return True, f"Successfully imported {imported_count} rooms", imported_count
    
    except FileNotFoundError:
        return False, f"File not found: {filename}", 0
    except Exception as e:
        return False, f"Error importing castle data: {str(e)}", 0
