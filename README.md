# Portafolio TurismoReal
### Requisitos:
Los requisitos necesarios para levantar la aplicacion TurismoReal con base de datos oracle son:
- Git [Descargar.](https://git-scm.com/downloads "Descargar.")
- Windows 7 o superior.
- Python 3.8.5 [Descargar.](https://www.python.org/downloads/release/python-385/ "Descargar.")
- Oracle Database 18c Express Edition for Windows x64 [Descargar.](https://www.oracle.com/database/technologies/xe-downloads.html "Descargar")
- SQL Developer [Descargar.](https://www.oracle.com/cl/tools/downloads/sqldev-v192-downloads.html "Descargar.")

### Como levantar la aplicación:


1. Ingresar como system en SQLDeveloper y crear el siguiente usuario:
```sql
create user c##turismoreal identified  by oracle;
grant connect, resource to c##turismoreal;
alter user c##turismoreal default tablespace users quota  unlimited  on users;
```
2. Escribir el siguiente comando en CMD en  una carpeta nueva para descargar el proyecto:
```shell
git clone https://github.com/bastipls/portafolio-departamentos
```
3. Cambiarse a la rama de ORACLE:
```shell
git pull dev-oracle
```
4. Luego entrar a la carpeta antes descargada y escribir el siguiente comando:
```shell
py -m venv myvenv
```
5. Activar el entorno virtual:
```shell
myvenv\Scripts\activate
```
6. Instalar requerimientos del proyecto con el entorno virtual activado:
```shell
pip install -r requirements.txt
```
7. Realizar migraciones:
```shell
py manage.py makemigrations
py manage.py migrate
```
8. Luego dirigirse otra vez a SQLDeveloper y crear los siguientes PL/SQL en el usuario creado al principo (c##turismoreal):
```sql
create procedure pl_listar_reservas_filtro(V_ID NUMBER, reservas_filtro out SYS_REFCURSOR)
as
begin
open reservas_filtro for
select *
from DEPARTAMENTOS_RESERVA
WHERE DEPARTAMENTO_ID = V_ID;
end;
/
create procedure pl_listar_checkouts(checkouts out SYS_REFCURSOR)
is
begin
open checkouts for select * from DEPARTAMENTOS_CHECK_OUT;
end;
/
```
8. Crear un superusuario:
```shell
py manage.py createsuperuser
```
9. Iniciar el proyecto
```shell
py manage.py runserver
```

