#!/usr/bin/env bash
#!/usr/bin/env bash
#!/usr/bin/env bash
set -eu



# Ativa venv existente ou cria e instala deps
if [ -f ".venv/bin/activate" ]; then
  . .venv/bin/activate
else
  python -m venv .venv
  . .venv/bin/activate
  pip install -U pip pytest pytest-cov mutmut
fi

# Coleta IDs dos sobreviventes
ids="$(python -m mutmut results | grep ': survived$' | cut -d: -f1 || true)"

if [ -z "${ids:-}" ]; then
  echo "Sem sobreviventes. Nada a reportar." | tee mutmut_survivors_report.txt
  exit 0
fi

# Gera relatório com diff de cada sobrevivente
: > mutmut_survivors_report.txt
for id in $ids; do
  {
    echo "===== $id ====="
    python -m mutmut show "$id"
    echo
  } >> mutmut_survivors_report.txt
done

echo "✔ Relatório salvo em mutmut_survivors_report.txt"
