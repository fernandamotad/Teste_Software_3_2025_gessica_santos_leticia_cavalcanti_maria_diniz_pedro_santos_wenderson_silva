import mutmut, mutmut.__main__ as mm

p = mm.__file__
print("mutmut.__main__ =>", p)

with open(p, "r", encoding="utf-8") as f:
    s = f.read()

t = "set_start_method('fork', force=True)"
s = s.replace("set_start_method('fork')", t)

with open(p, "w", encoding="utf-8") as f:
    f.write(s)

print("patched/applied")
