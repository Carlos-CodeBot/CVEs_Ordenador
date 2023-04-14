import sys
import re

# Obtener el nombre del archivo de entrada desde la línea de comando
if len(sys.argv) > 1:
    input_filename = sys.argv[1]
else:
    print("Error: se debe especificar un archivo de entrada.")
    sys.exit(1)

# Abrir el archivo de entrada y leer los CVEs
with open(input_filename, "r") as f:
    cve_pattern = re.compile(r'(CVE-\d{4}-\d{4,7})')
    cves = []
    for line in f:
        cves.extend(cve_pattern.findall(line))

# Ordenar los CVEs y escribirlos en un nuevo archivo
with open("output.txt", "w") as f:
    f.write(",\n".join(sorted(set(cves))))
    f.write("\n")
