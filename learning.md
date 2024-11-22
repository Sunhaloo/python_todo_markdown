# Date and Time Format

I knew that we have the `datetime` module in Python, but I did not really know how to really use it.
For my use case I wanted 2 types of "*datetime*" format.

```console
dd-MM-yyyy
HH:MM - dd/MM/yyyy
```

Then I learned about the `.now()` **method**. But the problem is that if you run $\downarrow$:

```python
from datetime import datetime
print(datetime.now())
```

The output that we are going to get looks something like this:

```console
2024-11-21 18:30:45.383694
```

But we **don't** want that! Hence, here comes `strftime()`... Our Saviour!
Therefore, we can simply pass in the "*format*" that we want and it will the date and/or time in the specified format.

```python
from datetime import datetime

# hence, we can have these
current_date = datetime.now().strftime("%d-%m-%Y")
datetime_header = datetime.now().strftime("%H:%M - %d/%m/%Y")
```

>[!NOTE]
>If you run these command that I show you from the Python Interpreter from the terminal. ( *or the program in you are on Windows* )
>Then the way that output is rendered / formatted is different.
>
>```python
># python 3.12.7
># its going to look something like this
>datetime.datetime(2024, 11, 21, 18, 43, 13, 462790)
>```
>
>BTW "*[All users of Windows are suckers!](https://www.youtube.com/watch?v=q9mXyakv2i8)*"

---

# Function to Check if Header is Present

```python
# create a function to check for header in the file
def check_header():
    # exception handling
    try:
        # open the file for read and check for header
        with open(file_name, 'r') as md_file:
            # make the contents for the file a list
            lines_in_file = md_file.readlines()

            # check for header
            return (len(lines_in_file) > 0) and (lines_in_file[0].startswith("#"))

    # if the file had not been found
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print(f"File '{current_date + ".md"}' has Not been Found at '{path}'\n")
```

>What is this function and why do we need it?

As you know we have our function `insert_task()` that will allow us to **append** task in the *markdown* file.
But the problem that I was facing was that; whenever I will go to insert **more** tasks ( *meaning that there was already some task(s)* ). It would also append the *header* **each** time that I would go to add something to the *list*:

```md
# Task for 20:46 - 21/11/2024

- [ ] Task 1
- [x] Task 2
# Task for 20:46 - 21/11/2024

- [ ] Task 3
- [x] Task 4
```

>Well, we don't want that!

## How does this Function works?

- Opens the file in **read** mode
- Convert all the lines in the file to a list with `.readlines()`
- Take only the first index $\rightarrow \ 0^{th}$ index
	- This is because the header will **only** exists at the top of the file.
- Check if the *header* exists

### How does it perform the check?

So I did not know this ( *obviously what do I know*! ), in Python, we have a **method** that can check if a string and its called `.startswith()`.
This method will accept a **character** or **string** as argument and will return either `True` or `False`.

Let me explain *me*, *myself* and *I* the line of code that actually checks for the header in the markdown file...

```python
return (len(lines_in_file) > 0) and (lines_in_file[0].startswith("#"))
```

Well, remember that we converted all the lines in the file into a *list*. Hence, we can say that if the length of that list is *greater* than 0 **and** also if the contents at *index* **0** starts with the character `#` ( *because its a header / `heading 1`* ). This means that the header is <span style="color: lime;">present</span>!

Thus, as we have `return` in front; therefore this function can return **3** values... Yes! 3 values. Here me out...

```console
# Task for 20:46 - 21/11/2024 ==> Function returns `True`
Task for 20:46 - 21/11/2024 ==> Function returns `False`
 ==> Function returns `None`
```

>It returns `None` cause there are `None`things... Please forgive me.

>[!INFO]
>Link to Python Documentation: https://docs.python.org/3/library/stdtypes.html#str.startswith

---

# I had to use Read and Write Mode...

So in most programming languages, we have different *modes* of creating, opening, writing and appending to / from a file.
Most of the time ( *we are talking about Python here* ), I will either use the:

- `x` $\Rightarrow$ Create a File
- `r` $\Rightarrow$ Read a File
- `w` $\Rightarrow$ Write to a File
- `a` $\Rightarrow$ Append to a File

But we also have others like `x+`, `a+` and [more](https://docs.python.org/3/library/functions.html#open)

I wanted to use the `a+` mode to check off tasks. Again, what do I mean by "*check off*"; look below $\downarrow$:

```md
- [ ] Task y --> Active Task
- [x] Task y --> Completed / Checked-Off Task
```

Basically, the `a+` mode allow one to *append* **and** also *read* from that file. But I had issues.

## Nevertheless

I learned something kinda weird and awesome about this `a+` mode.

So, when you open a file in **write** $\Rightarrow$ `w` mode. The "*cursor*" is placed at the top of the file. Hence, if you write something, close and then re-open to **write** to the file again. All previous contents will be lost even if it has been saved!

While in our little **append** $\Rightarrow$ `a` mode. We don't have the problem of our contents in the file being over-written.
This is because the "*cursor*" is placed at the bottom of the file. Hence, we can continue "*append*" safely without our data/contents being lost.

So let's say that you have this text file below:

<p align="center"><code>text.txt</code></p>

```console
The quick brown fox jumps over the lazy dog!
```

Let's now go ahead and **read** this file with the `a+` mode!

```python
import os

def main():
    # using `a+` mode to read the file
    with open(os.path.expanduser("~/Desktop/test.txt"), "a+") as file:
        # place the contents of file in list
        contents = file.readlines()

        # output the contents
        print(contents)


if __name__ == '__main__':
    main()
```

Well, you would expect our list to have something like:

```console
'The quick brown fox jumps over the lazy dog!\n'
```

But our **true** output is:

```console
[]
```

>Well, Nothing!

### The Reason

So, from what I said earlier, different *mode* places the *cursor* or more technically the **pointer** at different spot in the file.
Hence, this is why a file get over-written when we use the `w` mode.

But, you should be saying well, the `a+`'s read mode is fucked up. No! its not, we need to simply place the cursor / pointer at the top of the file. We do this with the `.seek()` method.

```python
import os

def main():
    # using `a+` mode to read the file
    with open(os.path.expanduser("~/Desktop/test.txt"), "a+") as file:
        # place the pointer / cursor at the top of the file
        file.seek(0)

        # place the contents of file in list
        contents = file.readlines()

        # output the contents
        print(contents)


if __name__ == '__main__':
    main()
```

Now, our output will be correct:

```console
['The quick brown fox jumps over the lazy dog!\n']
```

>[!NOTE]
>I don't really remember why I stopped using the `a+` mode.
>But I think because it was going to be much more annoying and complicated for nothing. Hence, this is why I used the `r` and `w` modes.
>
>Then again, it accomplishes my tasks of "*checking-off*" our... *tasks*!

---

# I had to use Read and Write Mode...

So in most programming languages, we have different *modes* of creating, opening, writing and appending to / from a file.
Most of the time ( *we are talking about Python here* ), I will either use the:

- `x` $\Rightarrow$ Create a File
- `r` $\Rightarrow$ Read a File
- `w` $\Rightarrow$ Write to a File
- `a` $\Rightarrow$ Append to a File

But we also have others like `x+`, `a+` and [more](https://docs.python.org/3/library/functions.html#open)

I wanted to use the `a+` mode to check off tasks. Again, what do I mean by "*check off*"; look below $\downarrow$:

```md
- [ ] Task y --> Active Task
- [x] Task y --> Completed / Checked-Off Task
```

Basically, the `a+` mode allow one to *append* **and** also *read* from that file. But I had issues.

## Nevertheless

I learned something kinda weird and awesome about this `a+` mode.

So, when you open a file in **write** $\Rightarrow$ `w` mode. The "*cursor*" is placed at the top of the file. Hence, if you write something, close and then re-open to **write** to the file again. All previous contents will be lost even if it has been saved!

While in our little **append** $\Rightarrow$ `a` mode. We don't have the problem of our contents in the file being over-written.
This is because the "*cursor*" is placed at the bottom of the file. Hence, we can continue "*append*" safely without our data/contents being lost.

So let's say that you have this text file below:

<p align="center"><code>text.txt</code></p>

```console
The quick brown fox jumps over the lazy dog!
```

Let's now go ahead and **read** this file with the `a+` mode!

```python
import os

def main():
    # using `a+` mode to read the file
    with open(os.path.expanduser("~/Desktop/test.txt"), "a+") as file:
        # place the contents of file in list
        contents = file.readlines()

        # output the contents
        print(contents)


if __name__ == '__main__':
    main()
```

Well, you would expect our list to have something like:

```console
'The quick brown fox jumps over the lazy dog!\n'
```

But our **true** output is:

```console
[]
```

>Well, Nothing!

### The Reason

So, from what I said earlier, different *mode* places the *cursor* or more technically the **pointer** at different spot in the file.
Hence, this is why a file get over-written when we use the `w` mode.

But, you should be saying well, the `a+`'s read mode is fucked up. No! its not, we need to simply place the cursor / pointer at the top of the file. We do this with the `.seek()` method.

```python
import os

def main():
    # using `a+` mode to read the file
    with open(os.path.expanduser("~/Desktop/test.txt"), "a+") as file:
        # place the pointer / cursor at the top of the file
        file.seek(0)

        # place the contents of file in list
        contents = file.readlines()

        # output the contents
        print(contents)


if __name__ == '__main__':
    main()
```

Now, our output will be correct:

```console
['The quick brown fox jumps over the lazy dog!\n']
```

>[!NOTE]
>I don't really remember why I stopped using the `a+` mode.
>But I think because it was going to be much more annoying and complicated for nothing. Hence, this is why I used the `r` and `w` modes.
>
>Then again, it accomplishes my tasks of "*checking-off*" our... *tasks*!

---

# Socials

- **Instagram**: https://www.instagram.com/s.sunhaloo
- **YouTube**: https://www.youtube.com/channel/UCMkQZsuW6eHMhdUObLPSpwg
- **GitHub**: https://www.github.com/Sunhaloo

---

S.Sunhaloo
Thank You!
