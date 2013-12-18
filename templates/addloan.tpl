<h1>Add {{table}}</h1>

<p>Please Fillout student information</p>
<form method="post" action="/added/loans">
  <input name="person_id" type="hidden" value="{{person['person_id']}}">
  <input name="person_fname" type="hidden" value="{{person['person_fname']}}">
  <input name="person_lname" type="hidden"  value="{{person['person_lname']}}">
  <label>Item Id</label>
  <select name="itemnum">
    %for option in items:
    <option value="{{option}}" style="width:  500px;">{{option}}</option>
    %end
  </select>
  <button type="submit">Submit</button>
</form>

%rebase templates/base.tpl title='Add Form'
