from fpdf import FPDF

# Classe para gerar o boletim em PDF
class BoletimPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Boletim Escolar', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

    def adicionar_boletim(self, nome_aluno, turma, notas):
        self.add_page()
        self.set_font('Arial', '', 12)

        # Informações do aluno
        self.cell(0, 10, f'Aluno: {nome_aluno}', 0, 1)
        self.cell(0, 10, f'Turma: {turma}', 0, 1)
        self.ln(10)

        # Tabela de notas
        self.set_font('Arial', 'B', 12)
        self.cell(80, 10, 'Materia', 1, 0, 'C')
        self.cell(30, 10, 'Nota', 1, 0, 'C')
        self.cell(30, 10, 'Status', 1, 1, 'C')
        self.set_font('Arial', '', 12)

        for materia, nota in notas.items():
            status = 'Aprovado' if nota >= 6 else 'Reprovado'
            self.cell(80, 10, materia, 1, 0, 'C')
            self.cell(30, 10, f'{nota:.1f}', 1, 0, 'C')
            self.cell(30, 10, status, 1, 1, 'C')

# Função principal para gerar o boletim
def gerar_boletim():
    # Dados fictícios (podem ser substituídos por entrada do usuário ou arquivo CSV)
    nome_aluno = 'João da Silva'
    turma = '3º Ano A'
    notas = {
        'Matemática': 7.5,
        'Português': 5.0,
        'História': 8.0,
        'Geografia': 6.0,
        'Ciências': 4.5
    }

    # Gerando o boletim
    pdf = BoletimPDF()
    pdf.adicionar_boletim(nome_aluno, turma, notas)

    # Salvando o boletim em PDF
    pdf.output(f'{nome_aluno} | {turma} | boletim_escolar.pdf')
    print("Boletim gerado com sucesso: boletim_escolar.pdf")

# Executar o programa
if __name__ == "__main__":
    gerar_boletim()
