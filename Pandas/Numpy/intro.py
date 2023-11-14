# %%
# Import Python Modules
import numpy as np

# %% [markdown]
## np.ndarray
# float32 (a.k.a. float)
# float64 (a.k.a. double); default
# int32 (a.k.a. int)

# np.ndarray is highly-efficient data abstraction written in C with Python's bindings 
# for easier usage
# %%
nd_array1 = np.ndarray((2, 2))
print(nd_array1)
# %%

# np.array IS A FACTORY METHOD which creates np.ndarray (numpy N-dimensional array) objects
# Factory methods are methods which, dependent on the input we pass to it returns different object types
# Defining arrays
arr1d_int = np.array([1, 2, 3, 4])
arr2d_float = np.array(((1, 2, 3, 4), (5, 6, 7, 8.0)))  # Notice 8.0

print(arr1d_int)
print(arr2d_float)
arr1d_int.dtype, type(arr1d_int), arr2d_float.dtype, type(arr2d_float)

# %% [markdown]

## Changing data type
# There are two basic approaches to obtain that:
# Specifying during creation
# Casting via .astype (new array is created, THIS IS NOT DONE IN-PLACE as new array has to be

# Failed attempt, new array returned 
arr1d_int.astype("int8")
print(arr1d_int.dtype)

# Correct way, new object is assigned to itself
arr1d_int = arr1d_int.astype("int8")

arr1d_int.dtype
# %%
# We can also specify it as `np.TYPE` object
new_arr = np.array([1, 2, 3], dtype=np.int8) # or "int8" string
# %% [markdown]

# Data layout
## np.ndarray is kept in memory as 1D array of contiguous values
## Numpy has everything stored in a "single line", but it has an attribute called stride that helps to know how the data is distributed.

print(
    f"""Int1D itemsize: {arr1d_int.itemsize}
Int1D strides: {arr1d_int.strides}
Float2D itemsize: {arr2d_float.itemsize}
Float2D strides: {arr2d_float.strides}
    """
)

# itemsize - specifies how many bytes are used for the data type
# stride - specifies how many bytes we have to jump in order to move to the next element



# %%
# Explain values below based on the code and output

arr = np.arange(9).reshape(3, 3)

print(arr)
print(f'The data type of each element is: {arr.dtype}')
print(f'The length of each element in bytes is: {arr.itemsize}')
print(f'The strides of the data types is: {arr.strides}')

# %%
# Transpose 
transposed = arr.T

print(transposed)
transposed.strides

# %% [markdown]
### Shape
# <our_array>.shape returns dimensionality of <our_array>

# It is one of the most often used attributes in numpy and scientific computing so keep that in mind!

### Creating np.ndarrays

# Numpy allows us to easily create data in multiple ways, namely:

# From standard Python structures (lists or tuples) (possibly nested)
# Direct creation of np.ndarray via:
# random operations (elements are taken from some distribution)
# using single value (zeros, ones, eye with some value)
# Let's see a few creation operations (all of them are listed here: https://numpy.org/doc/stable/reference/routines.array-creation.html). 
# Usually, the arguments we pass to them is the dimensions we want to give to the matrix




# %% 
ones = np.ones((3, 2)) # 2D matrix filled with ones
zeros = np.zeros_like(ones) # 2D zero matrix filled with zeros of the same shape as ones and zeros
identity = np.eye(3)
xeros = np.zeros((3,2))
print(ones)
print(f'Shape of "one" is: {ones.shape}')
print(zeros)
print(f'Shape of "zeros" is: {zeros.shape}')
print(identity)
print(f'Shape of "identity" is: {identity.shape}')
print(xeros)
print(f'Shape of "xeros" is: {xeros.shape}')
# %% [markdown]
### Creating random np.array

# numpy provides means to create random arrays (for example defined by some distribution)

# Here: https://numpy.org/doc/stable/reference/random/index.html  you can see a full list of possibilities, all of them are located in random module.

# Example usage:


# %%
vals = np.random.standard_normal(10)

vals
# %%
vals = np.random.randn(3, 4)

vals
# %%
vals = np.random.rand(3, 4)

vals
# %%
# Create a NumPy array with 5 elements of your choice.

arr5 = np.array([1,2,3,4,5])
arr5
type(arr5)
arr5.dtype
# %%
# Display the 5th element of the array
arr5[4]
# %%
# Use the np.random.randint function to create a 2D array of size (3,4) with random integers between 0 and 10.

new_vals1 = np.random.randint(0, 10, (3,4))
print(f"new_vals1: {new_vals1}")
# %% [markdown]

## Array Operations
### addition: +
### - subtraction: -
### - multiplication: *
### - bitwise operations (when array is boolean)
# Other examples here: https://scipy-lectures.org/intro/numpy/operations.html 



# %%
arr1 = np.full((3, 3), fill_value = 5)
identity_1 = np.eye(arr1.shape[0], dtype='int64')
print(arr1)
print('    +    ')
print(identity_1)
print('    =    ')
print(arr1 + identity_1)
# %% [markdown]

### Mathematical functions
# numpy provides a lot of math functions (e.g. trigonometric)

# Traits:

# Works on any array (usually element-wise) with some edge-case exceptions
# Optimized C implementations
# Provided in the np namespace
# All available operations are listed here
# %%
# np.e and np.pi are predefined constant

(np.cos(arr1) - np.sin(arr1) ** 3) / (np.eye(arr1.shape[0]) * np.e + 0.1)
# %% [markdown]
# Linear algebra operations
# numpy provides linear algebra functionalities located within np.linalg submodule
# See https://numpy.org/doc/stable/reference/routines.linalg.html 

# Inner dimensions must match!

X, y = np.random.randn(10, 6), np.random.randn(6, 3)

(X @ y).shape





# %%
x = np.ndarray((2, 3))
x
# %%
A = np.random.randn(10)
B = np.random.randn(10)

np.inner(A, B)
# %%
# Eigen values

np.linalg.eig(np.random.randn(10, 10))
# %% [markdown]
# numpy allows us to access data in multiple ways
# ALWAYS USE numpy OPERATIONS
# NO FOR LOOPS KNOWN FROM PYTHON (every operation you do should be done purely in numpy)
# %%
# Standard index-based item
# create a 2D array 

matrix = np.arange(20).reshape(5, 4)

matrix

# %%
# Obtaining single element

matrix[0, 0], matrix[1, 0], matrix[0, 1], matrix[2][0], matrix[1][3]
# %%
# first row

matrix[0]
# %%
# : means all elements
# 0 means 0th column

matrix[:, 0]
# %%
# Rows from second upwards
matrix[2:]
# %%
# Columns from second upwards
matrix[:, 2:]
# %%
# Rows from zeroth to third, column 0
matrix[:3, 0]
# %%
# Inverse of columns

matrix[:, ::-1]
# %%
matrix[::-1, ::-1]
# %%
matrix[::-3, ::-2]
# %%
# change to 3D tensor
temp = matrix.reshape(2, 2, -1)
temp.shape
# %%
# Same as temp[:, :, -1] e.g. last element from last dimension
# Rest left in-tact
# 2, 2 as we have created five 2,2 matrices

temp[..., -1]
# %%
# Fancy indexing
matrix


# %%
# Column 0 and 2
matrix[:, [0, 2]]
# %%
# Take last row twice

matrix[[-1, -1]]
# %%
# Shuffle rows using indices

indices = np.arange(matrix.shape[0])
print(indices)
permuted = np.random.permutation(indices)
print(permuted)

matrix[permuted]
# %%
# Obtain rows based on boolean values

matrix[[True, True, False, True, False]]
# %%
# Obtaining only elements which fulfill condition
# In this case elements larger than 5

print(matrix > 5)

# Array has to be flat as it lost it's N x N structure
matrix[matrix > 5]
# %%
# Create a NumPy array of random numbers with dimensions 6 x 10. Call it my_array
# my_array = np.random.randn(6, 10)
my_array = np.ndarray((6,10))*10
my_array
# %%
# Slice out the 1st, 3rd and 5th column of the array into as new array. Call it new_array
new_array = my_array[:,[0,2,4]]
new_array
# %%
# Print the shape of each array you have created.

print(f"Shape of my_array: {my_array.shape}\n" )
print(f"Shape of my new_array: {new_array.shape}\n")
# %%
# Try to multiply new_array x my_array. Does it work? If not, do you know why?
new_array * my_array
# (6x10) * (6X3). It can only work if (6X10)*(10X3) or (6X3)(3X10) etc.
# Inner dimensions must match!
# Mismatch in Dimension
# %%
# Transpose new_array and try again. Does it work now?
new_array_transposed = np.transpose(new_array)
# or
# new_array_transposed = (new_array).T
new_array_transposed
new_array_transposed.shape
# %%
product = np.matmul(new_array_transposed, my_array)
product


# %%

new_array #array
print(new_array)

print(f"\nshape of array: {new_array.shape} \n") # shape of array

print(f"data type of array: {new_array.dtype} \n") # data type of array - i.e int64 is 64 bits = 8 bytes 

print(f"dimension of array: {new_array.ndim}\n") #dimension of array

print(f"No. of Elements: {new_array.size}\n") # number of elements

print(f"Size of each element in bytes: {new_array.itemsize}\n") # size in bytes of each element



# %%
print(f"\nprint an element of array: {new_array[0]} \n") # shape of array
# %%
l =[1,2,3] #list
a=np.array([1,2,3]) #array

print(f"List: {l}\n")
print(f"Array: {a}\n")

l.append(4)
print(f"List with addition: {l}\n")
l = l + [5]
print(f"List with addition new element added: {l}\n")
# a.append(4) # will not work
# print(f"Array with addition: {a}\n")
a= a + np.array([4])
print(f"Array with addition new element added: {a}\n")
# %%
# Multipication

l = l * 2
print(f"List with multipication new element added: {l}\n")
a= a *2
print(f"Array with multipication new element added: {a}\n")
# %%
# sqrt 
a = np.sqrt(a)
print(a)
# %%
# dot product
l1 =[1,2,3] #list
l2 = [4, 5, 6]
a1=np.array(l1) #array
a2=np.array(l2)
# naive approach
dot = 0
for i in range(len(l1)):
    dot += l1[i]*l2[i]

print(f"dot: {dot}")

# better approach
dot2 = np.dot(a1,a2)
print(f"dot2: {dot2}")

# or

sum1 = a1 * a2
print(f"sum1: {sum1}")
dot3 = np.sum(sum1)
print(f"dot3: {dot3}")


# or

dot4 = (a1 * a2).sum()
print(f"dot4: {dot4}")

# or new version

dot5 = a1 @ a2
print(f"dot5: {dot5}")

# %% [markdown]
### Reshape and view
# .reshape(x, y, z) will change the way we access our array

# It is important to note that:

# reshape USUALLY DOES NOT COPY UNDERLYING DATA (it is merely changing strides and the way we access it)
# COPY OF np.ndarrays IS USUALLY NOT DONE (unless necessary)
# It almost never creates any problem for us (as long as we're working with numpy reasonably)
# %%
# .reshape(x, y, z) will change the way we access our array

# elements 0-18 reshaped into
# 
# creates a NumPy array named arr containing numbers from 0 to 17 (18 numbers in total).
arr = np.arange(18)
# 
print(arr)

print(arr.shape, arr.strides)
# prints the shape and strides of the original array arr. 
# The shape is the size of each dimension of the array, 
# and strides define the number of bytes to step in each dimension 
# when traversing the array.

reshaped = arr.reshape(3, 2, -1)

# In this line, the array arr is reshaped into a new array named reshaped with dimensions 3x2x(remaining), 
# where the -1 is a placeholder that means the size in that dimension is inferred 
# so that the total number of elements remains the same. In this case, 
# the total number of elements in the reshaped array is the same as in the original array.

print(reshaped.shape, reshaped.strides)

# Here, it prints the shape and strides of the reshaped array.

print(f"Sharing underlying memory: {np.may_share_memory(arr, reshaped)}")

# Finally, this line prints whether the original array arr and the reshaped array reshaped share the underlying memory. 
# This is a check to see if changes in one array would affect the other.

# %%
# Will change both arrays
arr[7] = 99999.

print(arr)
print(reshaped)
# %%
X1 = np.random.randn(128, 10)
print(X1)
X2 = np.random.rand(1280)
print(X2)
# %% [markdown]
# -1 in reshape

# -1 is used in order to infer missing dimensionality

# It is pretty useful when:

# we don't know some dimension beforehand
# we write function that has to work independently of some dimension


# %%
np.random.randn(5, 6, 8).reshape(-1, 10).shape
# %%
def make_second_dimension_10(array):
    assert array.size % 10 == 0, "Number of array elements has to be dividable by 10"
    return array.reshape(-1, 10)

# This defines a function make_second_dimension_10 that takes an array as input. 
# Here's what it does:
# It checks whether the total number of elements in the input array is divisible by 10 
# using the assertion assert array.size % 10 == 0. 
# If it's not, an error message is raised indicating that the number of array elements must be divisible by 10.

# If the assertion passes, it reshapes the array using array.reshape(-1, 10). 
# The -1 in the reshape function is a placeholder 
# that means the size in that dimension is inferred so that the total number of elements remains the same. 
# In this case, it's used to reshape the array into a 2D array with the second dimension having a size of 10.

print(make_second_dimension_10(np.random.randn(5, 6, 8)).shape)
# This line generates a random 3D array with shape (5, 6, 8) using np.random.randn and 
# then calls the make_second_dimension_10 function on it. It prints the shape of the resulting array, 
# which is reshaped to have the second dimension equal to 10.
make_second_dimension_10(np.random.randn(120)).shape
# This line generates a random 1D array with 120 elements using np.random.randn and 
# then calls the make_second_dimension_10 function on it. 
# It returns the shape of the resulting array, which should be a 2D array with the second dimension equal to 10.



# %%
### Broadcasting
# Broadcasting means automatic expansion of smaller array to a larger one
(np.array([[1], [2], [3]]) * np.array([[1, 2]])).shape


# %%
# Broadcasting for both arrays

arr1 = np.random.randn(10, 3)
# This line creates a NumPy array arr1 with a shape of (10, 3), meaning it's a 2D array with 10 rows and 3 columns. The values in this array are random samples from a standard normal distribution (mean 0 and standard deviation 1).
arr2 = np.random.randn(10, 5)
# This line creates another NumPy array arr2 with a shape of (10, 5), meaning it's a 2D array with 10 rows and 5 columns. Like arr1, the values in this array are random samples from a standard normal distribution.
result = arr1.reshape(-1, 1, 3) * arr2.reshape(10, -1, 1)
# arr1.reshape(-1, 1, 3): This reshapes arr1 into a 3D array with the new shape (10, 1, 3). The -1 in the reshape function is a placeholder that means the size in that dimension is inferred so that the total number of elements remains the same.
# arr2.reshape(10, -1, 1): This reshapes arr2 into a 3D array with the new shape (10, 5, 1).
# The multiplication (*) between these reshaped arrays performs element-wise multiplication. Broadcasting is used to match the dimensions for multiplication.
result.shape
# This line prints the shape of the resulting array result after the element-wise multiplication. The shape is determined by broadcasting rules, and in this case, it should be (10, 5, 3).

# %%
# Will not work
a = np.random.randn(1, 10)
b = np.random.randn(3)

a + b

# NumPy cannot align the shapes for broadcasting because the first dimension of a is 1, and the first dimension of b is 3.
# %%
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([0, 2, 0]).reshape(3, 1)

x * y
# %%
a = np.random.randn(3, 3)
b = np.random.randn(3)

a - b
# Here, the shape of a is (3, 3), and the shape of b is (3). Now, the broadcasting works because NumPy can align the dimensions. The second dimension of a is 3, and the first dimension of b is also 3, so NumPy can broadcast them, resulting in an addition operation.
# %%
# numpy is a framework which allows us to work with N dimensional arrays.
# we will define many tasks in terms of dimensions and what each dimension represents.
# An example could be data of shape (users, movies) which specifies:

# Ratings given for a movie
# For every user
# For every movie

users = 24
movies = 10

data = np.random.randint(0, 11, size=(users, movies)) # 11 as it's one more than maximum 10 score
# np.random.randint(0, 11, [24,10])
data



# %%
# data: (users, movies)
# find average rating for each user:
# total_ratings: (users,)
total_ratings = data.sum(axis=1) # sum all of the columns
print(total_ratings)
# mean_ratings: (users,)
mean_ratings = total_ratings / data.shape[1] # divide by total number of available movies

print(mean_ratings)
# %%
# Average rating for a movie (almost the same as previously, just changing dimensions!):

# data: (users, movies)

# total_ratings: (movies,)
total_ratings = data.sum(axis=0) # sum all of the rows

# mean_ratings: (movies,)
mean_ratings = total_ratings / data.shape[0] # divide by total number of users which gave the movie rating

print(mean_ratings)
# %%
# Highest rating gave for any movie by specific user:
data.max(axis=1)
# %%
#Which movie (movie index) got the lowest score for each user:
data.argmin(axis=1)
# %%
# which one was scored the lowest amongst all users:

# Movie which got the lowest score per-user

lowest = data.argmin(axis=1) # (users, )

# Calculate how often each lowest value occured
# minlength specifies number of entries (10 in our case as there are 10 movies)

counts = np.bincount(lowest, minlength=data.shape[1]) # (movies,)
print(counts)
# Get movies which got lowest rated most frequently:

np.argmax(counts) # (1, )
# %%
# Create a NumPy 1D-array with 10 elements, then reshape the array into a 2x5 matrix.

test_array = np.random.rand(10)
test_array

test_array.reshape(2,5)

# %%
# Create a second NumPy array with 5 elements, and join it to the first array using the concatenate function.

test_array2 = np.random.randint(0,5, size=5)
print(test_array2)

# Join the two arrays using np.concatenate
result_array = np.concatenate((test_array, test_array2))
print("\nResult Array: ")
print(result_array)
# %%
