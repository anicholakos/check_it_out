<h1>Remove loan</h1>

<p>Please Fillout student information</p>
<form method="post" action="">
  <label>Person Name<select>
    %for option in loaned:
      <option value={{option}}>{{option}}</option>
    %end
  <input type="submit">
</form>

%rebase templates/base.tpl title='Add Form'
