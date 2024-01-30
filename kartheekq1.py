import matplotlib.pyplot as plt

def plot_histogram(file_name, output_file):
    # Full path to the file
    full_path = f'/home/kali/Downloads/Scripts/{file_name}'

    # Read data from the file
    with open(full_path, 'r') as file:
        data = [line.split() for line in file]

    # Extract addresses based on the operation type
    read_addresses = [int(addr, 16) for op, addr in data if op == '0']
    write_addresses = [int(addr, 16) for op, addr in data if op == '1']
    fetch_addresses = [int(addr, 16) for op, addr in data if op == '2']

    # Create histograms for each operation
    plt.hist(read_addresses, bins=50, range=(min(read_addresses), max(read_addresses)), edgecolor='black', label='Read')
    plt.hist(write_addresses, bins=50, range=(min(write_addresses), max(write_addresses)), edgecolor='black', label='Write', alpha=0.7)
    plt.hist(fetch_addresses, bins=50, range=(min(fetch_addresses), max(fetch_addresses)), edgecolor='black', label='Fetch', alpha=0.7)

    # Set labels and title
    plt.xlabel('Address (Decimal)')
    plt.ylabel('Occurrences')
    plt.title(f'Histogram - {output_file}')
    
    # Add legend
    plt.legend()

    # Save the plot as a PNG file
    plt.savefig(f'/home/kali/Downloads/Scripts/{output_file}')

    # Show the plot (optional)
    plt.show()

# Plot histogram for cc1.din
plot_histogram('cc1.din.txt', 'cc1_histogram1.png')

# Plot histogram for spice.din
plot_histogram('spice.din.txt', 'spice_histogram1.png')

def calculate_operation_frequency(file_name):
    # Full path to the file
    full_path = f'/home/kali/Downloads/Scripts/{file_name}'

    # Read data from the file
    with open(full_path, 'r') as file:
        data = [line.split()[0] for line in file]

    # Count the occurrences of each operation type
    read_count = data.count('0')  # '0' represents read operation
    write_count = data.count('1')  # '1' represents write operation
    fetch_count = data.count('2')  # '2' represents instruction fetch operation

    return read_count, write_count, fetch_count

# Calculate operation frequencies for cc1.din
cc1_read_count, cc1_write_count, cc1_fetch_count = calculate_operation_frequency('cc1.din.txt')

# Calculate operation frequencies for spice.din
spice_read_count, spice_write_count, spice_fetch_count = calculate_operation_frequency('spice.din.txt')

# Print the results
print(f"Frequency of Writes (cc1): {cc1_write_count}")
print(f"Frequency of Reads (cc1): {cc1_read_count}")
print(f"Frequency of Fetches (cc1): {cc1_fetch_count}")
print(f"Frequency of Writes (spice): {spice_write_count}")
print(f"Frequency of Reads (spice): {spice_read_count}")
print(f"Frequency of Fetches (spice): {spice_fetch_count}")

