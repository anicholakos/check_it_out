<h1>Remove loan</h1>

<p>Please Fillout student information</p>
<form method="post" action="/removing">
  <label>Person Name</label>
    <select name="person_lname">
      %for option in loaned:
        <option value={{option}}>{{option}}</option>
      %end
    </select>
  <label>ID Number</label>
    <select name="item_name">
    %for itemop in items:
      <option value={{itemop}}>{{itemop}}</option>
    %end
    </select>
  <input type="submit">
</form>

%rebase templates/base.tpl title='Add Form'
