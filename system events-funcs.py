
def id_warning_patterns(file_path, pattern_length=3):
    """  
    Identifies patterns of warning events in the log file.

    Parameters:
        file_path (str): Path to the file.
        pattern_length (int): Number of warning events to form a pattern. Default is 3.

    Returns:
        dict: Patterns with occurrences greater than 1.
    """
        
    warning_patterns = {}  

    with open(file_path, 'r') as file:
        logs = file.readlines()

    event_sequence = []

    for line in logs:
        parts = [part.strip() for part in line.split('|')]
        if len(parts) < 4:
            continue

        event_type = parts[1]
        event_desc = parts[3]

        if event_type == "Warning":
            event_sequence.append((event_type, event_desc))

        if len(event_sequence) >= pattern_length:
            
            pattern = tuple(event_sequence[-pattern_length:])

            warning_patterns[pattern] = warning_patterns.get(pattern, 0) + 1

    significant_patterns = {pattern: count for pattern, count in warning_patterns.items() if count > 1}
    return significant_patterns



log_file_path = "C:/Users/steph/Downloads/spring2024_system_events.txt"
pattern_length = 3
patterns = id_warning_patterns(log_file_path, pattern_length=pattern_length)

for i, (pattern, count) in enumerate(patterns.items(), start=1):
    events = " -> ".join(f"{event[1]}" for event in pattern) 
    print(f"{i}. Pattern: {events} | Occurrences: {count}")

        