# Database


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `branch_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | The ID of the branch to which the database belongs<br/>              |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | A timestamp indicating when the database was created<br/>            |
| `id`                                                                 | *int*                                                                | :heavy_check_mark:                                                   | The database ID<br/>                                                 |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The database name<br/>                                               |
| `owner_name`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The name of role that owns the database<br/>                         |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | A timestamp indicating when the database was last updated<br/>       |