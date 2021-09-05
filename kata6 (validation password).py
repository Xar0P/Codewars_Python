# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python
# SUCESS

from re import search

regex="(?=[a-zA-Z0-9]{6})(?=[a-zA-Z0-9]+[a-z]|^[a-z])(?=[a-zA-Z0-9]+[A-Z]|^[A-Z])(?=[a-zA-Z0-9]+[0-9]|^[0-9])^[a-zA-Z0-9]*$" 
# "^\w*$" Tem espaço em branco ou tem caracteres não alphanumericos? Depois verifica se começa com \w* e termina com \w*
# (?=) É um fator de validação, retorna true ou false, tendo varios, é como se fosse "and"
# (?!) É um fator de negação, como se fosse o operador not


print(search(regex, 'Password123_'))