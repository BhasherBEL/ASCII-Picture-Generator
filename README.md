# _ASCII Picture Generator_

---

## _Abstract_

---

__ASCII Picture Generator__ is a small script written in python who convert a picture to an ASCII art text file.

## _Requirements_

---

- Python3.x
- PIL
- numpy

## _Usage_

---

- Minimal configuration

```python
asciigen.py picture.jpg
```

- Avanced configuration

```python
asciigen.py picture.jpg output.txt 100x100 complex
```

- Display help

```python
asciigen.py
```

Output:

```python
Usage: asciigen.py <from_path> [to_path=out.txt] [size=200x200] [mode=simple|complex]
```