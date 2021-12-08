import pandas as pd

def conversaodeMB(tamanhoMb):
  tamanhoMb = float(tamanhoMb)
  return (float(tamanhoMb/(1024*1024)))

def percentualPorUsuario(lista, total):
  percentual = (lista[3]/total)*100
  lista.insert((len(usuario)),percentual)