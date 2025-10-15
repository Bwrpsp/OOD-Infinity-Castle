import time
import psutil
import os
import csv
from datetime import datetime

class PerformanceTracker:
    def __init__(self):
        self.process = psutil.Process(os.getpid())
        self.metrics = []
        
    def start_tracking(self, command_name):
        return {
            'command': command_name,
            'start_time': time.time(),
            'start_ram': self.process.memory_info().rss / 1024 / 1024,  # Convert to MB
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def end_tracking(self, tracking_data):
        end_time = time.time()
        end_ram = self.process.memory_info().rss / 1024 / 1024  # Convert to MB
        
        metric = {
            'timestamp': tracking_data['timestamp'],
            'command': tracking_data['command'],
            'execution_time': round(end_time - tracking_data['start_time'], 4),
            'start_ram_mb': round(tracking_data['start_ram'], 2),
            'end_ram_mb': round(end_ram, 2),
            'ram_change_mb': round(end_ram - tracking_data['start_ram'], 2),
            'peak_ram_mb': round(self.process.memory_info().rss / 1024 / 1024, 2)
        }
        
        self.metrics.append(metric)
        return metric
    
    def export_to_csv(self, filename=None):
        if not self.metrics:
            return False, "No metrics to export"
        
        if filename is None:
            filename = f"performance_metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['timestamp', 'command', 'execution_time', 'start_ram_mb', 
                             'end_ram_mb', 'ram_change_mb', 'peak_ram_mb']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for metric in self.metrics:
                    writer.writerow(metric)
            
            return True, filename
        except Exception as e:
            return False, str(e)
    
    def get_summary(self):
        if not self.metrics:
            return "No metrics recorded yet."
        
        total_time = sum(m['execution_time'] for m in self.metrics)
        avg_time = total_time / len(self.metrics)
        max_ram = max(m['peak_ram_mb'] for m in self.metrics)
        
        summary = f"\n{'='*60}\n"
        summary += f"Performance Summary\n"
        summary += f"{'='*60}\n"
        summary += f"Total Commands Executed: {len(self.metrics)}\n"
        summary += f"Total Execution Time: {total_time:.4f} seconds\n"
        summary += f"Average Execution Time: {avg_time:.4f} seconds\n"
        summary += f"Peak RAM Usage: {max_ram:.2f} MB\n"
        summary += f"{'='*60}\n"
        
        return summary
    
    def clear_metrics(self):
        self.metrics = []
