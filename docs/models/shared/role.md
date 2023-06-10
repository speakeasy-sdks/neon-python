# Role


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `branch_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | The ID of the branch to which the role belongs<br/>                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | A timestamp indicating when the role was created<br/>                |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The role name<br/>                                                   |
| `password`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The role password<br/>                                               |
| `protected`                                                          | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Whether or not the role is system-protected<br/>                     |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | A timestamp indicating when the role was last updated<br/>           |