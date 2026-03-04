# 🧠 GUÍA RÁPIDA GIT – Sebastian Begazo

---

## 🚀 1️⃣ Crear proyecto nuevo y subirlo

```bash
mkdir nombre_proyecto
cd nombre_proyecto
git init
git remote add origin https://github.com/TU_USUARIO/NOMBRE_REPO.git
git add .
git commit -m "Primer commit"
git branch -M main
git push -u origin main
```

---

## 🔄 2️⃣ Subir cambios normales (repo ya conectado)

```bash
git status
git add .
git commit -m "Descripcion clara del cambio"
git push
```

---

## 📁 3️⃣ Crear carpeta y organizar archivos

```bash
mkdir nueva_carpeta
mv archivo.py nueva_carpeta/
git add .
git commit -m "Organizar estructura"
git push
```

---

## 🔌 4️⃣ Cambiar repositorio remoto

```bash
git remote -v
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/NUEVO_REPO.git
git push -u origin main
```

---

## 🧨 5️⃣ Si un archivo no aparece en GitHub

```bash
git status
git add .
git commit -m "Agregar archivo faltante"
git push
```

---

## 🏆 Regla de Oro

Siempre que tengas duda:

```bash
git status
```

---

## 📌 Convención profesional

- Sin espacios
- Sin tildes
- Todo en minúsculas
- Separar con `_`

Ejemplo correcto:

```
modelo_confiabilidad.py
```

---