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


