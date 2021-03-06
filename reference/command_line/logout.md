### logout

The 'logout' command is used to log the current user out of the remote registry. 

```
Usage: spoon logout

<options> available:
     --format=VALUE         Use json format for output
```

#### Examples:

```
# Logout the current user
> spoon logout

spoonuser logged out at 8/25/2014 5:55:50 PM

# No action taken if a user isn't currently logged in
> spoon logout

You are not currently logged into Spoon
```

#### JSON output

When `--format=json` option was passed this command will provide output in JSON format. It will contain only an `exitCode` value or an `error` object if command failed.