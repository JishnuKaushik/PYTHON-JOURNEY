# String Methods Cheat Sheet

WELL MY CLAUDE SAYS THIS BOU ALLL THE SHIT ABOVE 
Here's a clean, organized cheat sheet for all the `str` methods — grouped by what they actually *do*, with examples you can scan quickly.Six categories, 42 methods, all searchable. Here's a quick orientation:

**Case** — changing letter case (`upper`, `lower`, `title`, etc.) — you'll use these constantly for cleaning text in ML pipelines.

**Search** — finding things inside strings. Know the `find` vs `index` difference cold: `find` returns `-1` on failure, `index` raises a `ValueError`. Exam-relevant.

**Validate (is*)** — all return `True`/`False`. The subtle trap: `isdigit()` returns `True` for `"²"` (superscript 2), but `isdecimal()` doesn't. For normal input validation, `isdecimal()` is usually what you actually want.

**Modify** — `strip()`, `replace()`, `removeprefix()`/`removesuffix()`. The `strip()` family is something you'll use every single time you process real-world CSV data in Pandas.

**Split/Join** — `split()` and `join()` are a pair. You split on one end, process, join back. Core data manipulation pattern.

**Format** — `format()` and f-strings (f-strings aren't a method but achieve the same goal — we'll cover those separately).

---

Since you're on **Day 4 (loops today)** — want to get into `for` loops, `while`, `range()`, `break`/`continue`? Or do you want me to quiz you on what you just covered in strings first? Your call.
