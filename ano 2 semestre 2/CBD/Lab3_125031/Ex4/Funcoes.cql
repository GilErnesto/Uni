-- UDF 1
CREATE FUNCTION bmi(altura FLOAT, peso FLOAT) CALLED ON NULL INPUT RETURNS float LANGUAGE java AS $$ return peso/(altura*altura);$$; 

-- UDF 2
CREATE FUNCTION numero_dias(data_entrada TIMESTAMP, data_saida TIMESTAMP) CALLED ON NULL INPUT RETURNS int LANGUAGE java AS $$
return (int)((data_saida.getTime() - data_entrada.getTime()) / 86400000L);
$$;

-- UDA 1
CREATE FUNCTION media_visitas_state(state tuple<int, int>, val int) CALLED ON NULL INPUT RETURNS tuple<int, int> LANGUAGE java AS $$
if (val != null) {
    state.setInt(0, state.getInt(0) + 1);
    state.setInt(1, state.getInt(1) + val.intValue());
}
return state;
$$;

CREATE FUNCTION media_visitas_final(state tuple<int, int>) CALLED ON NULL INPUT RETURNS double LANGUAGE java AS $$
double r = 0;
if (state.getInt(0) == 0) return null;
r = state.getInt(1);
r /= state.getInt(0);
return Double.valueOf(r);
$$;

CREATE AGGREGATE media_visitas_por_dia(int)
SFUNC media_visitas_state
STYPE tuple<int, int>
FINALFUNC media_visitas_final
INITCOND (0, 0);

-- UDA 2
CREATE FUNCTION media_duracao_state(state tuple<int, int>, val int) CALLED ON NULL INPUT RETURNS tuple<int, int> LANGUAGE java AS $$
if (val != null) {
    state.setInt(0, state.getInt(0) + 1);
    state.setInt(1, state.getInt(1) + val.intValue());
}
return state;
$$;

CREATE FUNCTION media_duracao_final(state tuple<int, int>) CALLED ON NULL INPUT RETURNS double LANGUAGE java AS $$
if (state.getInt(0) == 0) return null;
double media = (double) state.getInt(1) / state.getInt(0);
return Double.valueOf(media);
$$;

CREATE AGGREGATE media_duracao_consultas(int)
SFUNC media_duracao_state
STYPE tuple<int, int>
FINALFUNC media_duracao_final
INITCOND (0, 0);
