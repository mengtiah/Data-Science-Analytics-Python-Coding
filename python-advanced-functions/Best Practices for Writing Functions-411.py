## 2. Retrieving Docstrings ##

import inspect
raw_docstring = split_and_stack.__doc__
formatted_docstring =inspect.getdoc(split_and_stack)

## 3. Google Style Docstrings ##

def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.
    Args:
        content (str)
        letter (str)
    
    Returns:
        int
    """
    
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])

formatted_docstring=inspect.getdoc(count_letter)

## 4. Google Style Docstrings Continued ##

def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int
     
    Raises:
      ValueError: If `letter` is not a one-character string.
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])

formatted_docstring = inspect.getdoc(count_letter)

print(formatted_docstring)

## 5. Don't Repeat Yourself ##

#df['y1_z'] = (df['y1_gpa'] - df['y1_gpa'].mean()) / df['y1_gpa'].std()
#df['y2_z'] = (df['y2_gpa'] - df['y2_gpa'].mean()) / df['y2_gpa'].std()
#df['y3_z'] = (df['y3_gpa'] - df['y3_gpa'].mean()) / df['y3_gpa'].std()
#df['y4_z'] = (df['y4_gpa'] - df['y4_gpa'].mean()) / df['y4_gpa'].std()

def standardize(string):
    return (df[string] - df[string].mean()) / df[string].std()

df['y1_z'] = standardize('y1_gpa')
df['y2_z'] = standardize('y2_gpa')
df['y3_z'] = standardize('y3_gpa')
df['y4_z'] = standardize('y4_gpa')

    

## 6. Do One Thing ##

#INITIAL CODE
def find_mean(values):
    """Get the mean and median of a list of `values`

    Args:
      values (iterable of float): A list of numbers

    Returns:
      tuple (float, float): The mean 
    """
    mean = sum(values) / len(values)
    return mean

def find_median(values):
    """Get the mean and median of a list of `values`

    Args:
      values (iterable of float): A list of numbers

    Returns:
      tuple (float, float): The median
    """
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]

    return median

list_mean = find_mean([1,2,3])
list_median = find_median([1,2,3,4])

## 7. Pass by Assignment ##

a = [1, 2, 3]
b = a
a.append(4)
print(b)
b.append(5)
print(a)
a=42

## 10. Mutable and Immutable Variables Continued ##

def add_column(values, df=None):
    """Add a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
        values (iterable): The values of the new column
        df (DataFrame, optional): The DataFrame to update.
          If no DataFrame is passed, one is created by default.

    Returns:
        DataFrame
    """
    if df is None:
        df=pandas.DataFrame()
    df['col_{}'.format(len(df.columns))] = values
    return df
df_1 = add_column(values=range(10))
df_1 = df_2 = add_column(values=range(10))
