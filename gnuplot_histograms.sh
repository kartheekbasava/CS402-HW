#!/bin/bash

# Define the input files
cc1_file="cc1.din.txt"
spice_file="spice.din.txt"

# Function to generate histogram data
generate_histogram_data() {
    input_file=$1
    output_file=$2

    # Use awk to extract address information
    awk '{ print strtonum("0x" $2) }' "$input_file" |
    
    # Use sort to sort the addresses
    sort -n |

    # Use uniq and awk to count occurrences and format data
    uniq -c |
    awk '{ print $2, $1 }' > "$output_file"
}

# Generate histogram data for cc1.din
generate_histogram_data "$cc1_file" "cc1_histogram_data.txt"

# Generate histogram data for spice.din
generate_histogram_data "$spice_file" "spice_histogram_data.txt"

# Plot histograms using gnuplot
gnuplot -persist << EOF
    set term png
    set output 'cc1_histogram.png'
    set title 'Address Distribution - cc1.din'
    set xlabel 'Address (Decimal)'
    set ylabel 'Occurrences'
    set xrange [0:*]
    set yrange [0.1:*]  # Set a minimum value for the y-axis
    set logscale y
    plot 'cc1_histogram_data.txt' with impulses title 'cc1.din'

    set term png
    set output 'spice_histogram.png'
    set title 'Address Distribution - spice.din'
    set xlabel 'Address (Decimal)'
    set ylabel 'Occurrences'
    set xrange [0:*]
    set yrange [0.1:*]  # Set a minimum value for the y-axis
    set logscale y
    plot 'spice_histogram_data.txt' with impulses title 'spice.din'
EOF

