import matplotlib.pyplot as plt


length_of_contraction = []
time_between_contraction = []


def get_length_of_contractions():
	with open("length_of_contraction.txt", 'r') as file:
		for line in file:
			line = line.rstrip()
			line = float(line)
			length_of_contraction.append(line)

	print(length_of_contraction)


def get_time_between_contractions():
	with open("time_between_contractions.txt", 'r') as file:
		for line in file:
			line = line.rstrip()
			line = float(line)
			time_between_contraction.append(line)

	print(time_between_contraction)



def plot_graph():
	get_length_of_contractions()

	get_time_between_contractions()

# plot_graph()

# Plot the data


plt.plot(time_between_contraction, length_of_contraction)
plt.gca().invert_xaxis()

# Add labels to the axes
plt.xlabel('Time Between Contraction')
plt.ylabel('Length of Contraction')

# Add a title to the plot
plt.title('Length and Frequency of Contractions')

# Show the plot
plt.show()


