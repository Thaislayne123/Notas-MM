# ============================================================
#   SISTEMA DE NOTAS DE ALUNOS — PYTHON
#   Digite o nome do aluno e veja: notas, médias e faltas
# ============================================================

# ── BASE DE DADOS ─────────────────────────────────────────────
alunos = {
    "Jaqueline Santos": {
        "turma": "3º A",
        "semestre1": {"Matemática": 8.0, "Português": 7.0, "Ciências": 10.0, "História": 6.5, "Geografia": 6.0},
        "semestre2": {"Matemática": 9.0, "Português": 8.5, "Ciências": 7.5, "História": 7.0, "Geografia": 9.5},
        "faltas":    {"Matemática": 2,   "Português": 0,   "Ciências": 1,   "História": 4,   "Geografia": 1},
    },
    "Soffia Pereira": {
        "turma": "3º B",
        "semestre1": {"Matemática": 9.0, "Português": 6.5, "Ciências": 7.5, "História": 7.0, "Geografia": 9.5},
        "semestre2": {"Matemática": 7.9, "Português": 6.5, "Ciências": 9.0, "História": 6.5, "Geografia": 8.5},
        "faltas":    {"Matemática": 15,   "Português": 10,   "Ciências": 12,  "História": 14,   "Geografia": 17},
    },
    "Carlos Josue": {
        "turma": "2º A",
        "semestre1": {"Matemática":10.0, "Português": 9.5, "Ciências":10.0, "História": 9.0, "Geografia": 9.5},
        "semestre2": {"Matemática": 8.5, "Português":10.0, "Ciências": 9.0, "História":10.0, "Geografia": 9.0},
        "faltas":    {"Matemática": 0,   "Português": 1,   "Ciências": 0,   "História": 0,   "Geografia": 2},
    },
    "Manoel Ribeiro": {
        "turma": "1º C",
        "semestre1": {"Matemática": 3.5, "Português": 4.0, "Ciências": 3.0, "História": 3.0, "Geografia": 4.5},
        "semestre2": {"Matemática": 4.5, "Português": 4.5, "Ciências": 4.0, "História": 5.0, "Geografia": 4.5},
        "faltas":    {"Matemática": 1,  "Português": 2,  "Ciências": 3,  "História": 2,   "Geografia": 0},
    },
    "Josiano Catarini": {
        "turma": "2º B",
        "semestre1": {"Matemática": 7.0, "Português": 7.5, "Ciências": 6.5, "História": 8.0, "Geografia": 7.0},
        "semestre2": {"Matemática": 7.5, "Português": 8.0, "Ciências": 7.0, "História": 7.5, "Geografia": 8.5},
        "faltas":    {"Matemática": 10,   "Português": 15,   "Ciências": 10,   "História": 11,   "Geografia": 3},
    },
}

# ── FUNÇÕES ────────────────────────────────────────────────────

def status(media):
    if media >= 7.0:   return "✅ APROVADO"
    elif media >= 5.0: return "⚠️  RECUPERAÇÃO"
    else:              return "❌ REPROVADO"

def barra(valor, tam=14):
    p = int((valor / 10) * tam)
    return "█" * p + "░" * (tam - p)

def exibir_aluno(nome, d):
    s1, s2, ft = d["semestre1"], d["semestre2"], d["faltas"]
    materias = list(s1.keys())
    icones = {"Matemática":"🔢","Português":"📖","Ciências":"🔬","História":"🏛️","Geografia":"🌍"}

    print()
    print("╔" + "═" * 60 + "╗")
    print("║{:^60}║".format("📋  BOLETIM ESCOLAR"))
    print("╠" + "═" * 60 + "╣")
    print("║  Aluno : {:<50}║".format(nome))
    print("║  Turma : {:<50}║".format(d["turma"]))
    print("╠" + "═" * 60 + "╣")
    print("║  {:<12}  {:>5}  {:>5}  {:>6}  {:>5}  {:<14}║".format(
          "Matéria", "1ºSem", "2ºSem", "Média", "Faltas", "Situação"))
    print("║  " + "─" * 56 + "  ║")

    total_medias, total_faltas = [], 0

    for mat in materias:
        n1  = s1[mat]; n2 = s2[mat]
        med = (n1 + n2) / 2
        flt = ft[mat]
        total_medias.append(med)
        total_faltas += flt
        ico = icones.get(mat, "📚")
        st = status(med).split()[0] + " " + status(med).split()[1] if len(status(med).split()) > 1 else status(med)
        print("║  {} {:<11}  {:>5.1f}  {:>5.1f}  {:>5.1f}  {:>5}   {:<13}║".format(
              ico, mat, n1, n2, med, flt, status(med)[:13]))

    mg = sum(total_medias) / len(total_medias)
    print("║  " + "─" * 56 + "  ║")
    print("║  {:<14}  {:>5}  {:>5}  {:>5.1f}  {:>5}   {:<13}║".format(
          "MÉDIA GERAL", "", "", mg, total_faltas, status(mg)[:13]))
    print("╠" + "═" * 60 + "╣")

    # Barra de desempenho
    print("║  Desempenho : {} {:.1f}/10{:<21}║".format(barra(mg), mg, ""))
    print("║  Faltas tot.: {:<46}║".format(
          f"{total_faltas}  ⚠️  Atenção!" if total_faltas > 50 else f"{total_faltas}  ✅ Frequência OK"))
    print("╚" + "═" * 60 + "╝")


# ── PROGRAMA PRINCIPAL ─────────────────────────────────────────

def main():
    print()
    print("╔" + "═" * 60 + "╗")
    print("║{:^60}║".format("🎓  SISTEMA DE NOTAS ESCOLARES"))
    print("╠" + "═" * 60 + "╣")
    print("║  Alunos cadastrados:{:<40}║".format(""))
    for i, nome in enumerate(alunos.keys(), 1):
        print("║    {}. {:<54}║".format(i, nome))
    print("╚" + "═" * 60 + "╝")

    while True:
        print("\n  Digite o nome do aluno (ou 'sair' para encerrar):")
        entrada = input("  → ").strip()

        if entrada.lower() == "sair":
            print("\n  👋 Sistema encerrado. Até logo!\n")
            break

        if not entrada:
            continue

        # Busca parcial, sem case-sensitive
        encontrado = None
        for nome in alunos:
            if entrada.lower() in nome.lower():
                encontrado = nome
                break

        if encontrado:
            exibir_aluno(encontrado, alunos[encontrado])
        else:
            print(f"\n  ❌ Aluno '{entrada}' não encontrado.")
            print("  💡 Dica: tente digitar só parte do nome (ex: 'Ana', 'Bruno').")

main()