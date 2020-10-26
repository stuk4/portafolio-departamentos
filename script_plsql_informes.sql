create procedure pl_listar_reservas(reservas out SYS_REFCURSOR)
is

begin
    open reservas for select * from DEPARTAMENTOS_RESERVA;
end;
/

create procedure pl_listar_checkouts(checkouts out SYS_REFCURSOR)
is

begin
    open checkouts for select * from DEPARTAMENTOS_CHECK_OUT;
end;
/


