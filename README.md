![Rit banner](/docs/img/ritchie-banner.png)

## How to use this repository ?

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/installation)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal:

```bash
echo '{"provider":"Github", "name":"code-labs", "url":"https://github.com/GuillaumeFalourd/ritchie-code-labs", "priority":1}' | rit add repo --stdin
```

Finally, you can check if the repository has been imported correctly by executing the `rit list repo` command.
