% import model


<!DOCTYPE html>
<html>

<head>Vislice</head>

<body>
  <table>
    <tr>
      <td>
        <h3> {{igra.pravilni_del_gesla()}} </h3>
      </td>
    </tr>

    <tr>
      <td> Neuspeli poskusi:</td>
      <td> {{ igra.nepravilni_ugibi() }} </td>
    </tr>

    <tr>
      <td>Stopnja obešenosti:</td>
      <td> {{igra.stevilo_napak() }} </td>
    </tr>

    % if poskus == model.ZMAGA or poskus == model.PORAZ:
      <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
      </form>
    %else:
    <tr>
      <form action="/igra/{{id_igre}}" method="post">
      <input type="text" name="poskus">
      <input type="submit" value="Ugibaj">
      </form>
    </tr>
    %end
  </table>


</body>

</html>