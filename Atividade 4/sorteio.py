nCamisas = int(input())
for i in range(nCamisas):
    ganhador = 100000000000000000000000
    qAlunos,nsorteado = map(int,input().split())
    nAlunos = map(int,input().split())
    for posicao,aluno in enumerate(nAlunos):
        if abs(aluno-nsorteado)<ganhador:
            ganhador = abs(aluno-nsorteado)
            posicaoGanhador = posicao
    print(posicaoGanhador+1)