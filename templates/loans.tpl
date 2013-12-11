<table>
  <tr>
    <th>Person ID</th>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Item ID</th>
    <th>Item</th>
    <th>Date Checked Out</th>
  </tr>
  %for row in loaned:
  <tr>
    %for col in row:
    <td>{{col}}</td>
    %end
 </tr>
  %end
</table>
<a href='/remove-loan'>remove loan</a>

%rebase templates/base.tpl title='loans'
