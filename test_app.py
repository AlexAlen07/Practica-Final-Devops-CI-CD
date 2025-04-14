def test_hola_mundo():
    with open("index.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    assert "<h1>Bienvenidos a la Práctica Final DevOps CI/CD</h1>" in contenido
