import csv
from datetime import datetime

def export_castle_to_csv(castle, filename=None):

    if filename is None:
        filename = f"castle_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        # Get all rooms from the castle
        rooms = castle.get_all_csv()
        
        if not rooms:
            return False, "Castle is empty - no data to export"
        
        # Write to CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['room_number', 'demon_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for room in rooms:
                writer.writerow({
                    'room_number': castle.tran.full_forward(room.num),
                    'demon_id': room.demon
                })
        
        return True, filename
    
    except Exception as e:
        return False, f"Error exporting castle data: {str(e)}"
