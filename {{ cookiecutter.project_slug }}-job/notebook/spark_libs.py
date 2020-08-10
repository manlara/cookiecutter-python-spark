import os

def import_packages(packages=[]):
    """
    Return a string (or None) based on Maven packages to import

    Parameters
    ----------
    packages : list
        list of Maven coordinates to include
        e.g, mysql:mysql-connector-java:8.0.16
    """
    if len(packages):
        pkg_coord = ",".join(packages)
        return "--packages " + pkg_coord

def import_local_jars(directory, jars=[]):
    """
    Return a string (or None) based a directory and list of jar files

    Parameters
    ----------
    directory : str
        Absolute path to jar folder
    
    jars : list
        list of jar files to import
    """
    if len(files):
        jar_files = ",".join([
            os.path.join(directory, jar)
            for jar in jars
        ])
        return "--jars " + jar_files

def spark_submit(packages=None, local_jars=None, directory=""):
    """
    Constructs Spark submit parameters. 
    Essentially generates Spark environment with desired libraries
    """
    args = []
    if bool(packages):
        arg = import_packages(packages)
        args.append(arg)
    
    if bool(local_jars):
        arg = import_local_jars(directory, local_jars)
        args.append(arg)
    
    os.environ['PYSPARK_SUBMIT_ARGS'] = " ".join(args) + " pyspark-shell"
    print(f"Adding environment variable `PYSPARK_SUBMIT_ARGS`\n{os.environ['PYSPARK_SUBMIT_ARGS']}")
