--USE gold_db
--GO
--
--CREATE OR ALTER PROC CreateSQLServerlessView_gold @ViewName nvarchar(100)
--AS
--BEGIN
--	DECLARE @statement VARCHAR(MAX)
--	SET @statement = N'CREATE OR ALTER VIEW ' + @ViewName + 'AS 
--		SELECT 
--		*
--		FROM
--			OPENROWSET(
--				BULK ''https://.dfs.core.windows.net/gold/SalesLT/' + @ViewName + '/'',
--				FORMAT = ''DELTA''
--			) AS [result]'
--	EXEC (@statement)
--END
--GO

USE gold_db
GO

CREATE OR ALTER PROC CreateSQLServerlessView_gold @ViewName nvarchar(100)
AS
BEGIN
    -- Change the data type to NVARCHAR(MAX) to handle Unicode concatenation properly
    DECLARE @statement NVARCHAR(MAX)
    
    SET @statement = N'CREATE OR ALTER VIEW ' + QUOTENAME(@ViewName) + N' AS 
        SELECT 
            *
        FROM
            OPENROWSET(
                BULK ''https://dataengsg.dfs.core.windows.net/gold/SalesLT/' + @ViewName + '/'',
                FORMAT = ''DELTA''
            ) AS [result]'
            
    -- Use sp_executesql for executing dynamic NVARCHAR strings safely
    EXEC sp_executesql @statement
END
GO