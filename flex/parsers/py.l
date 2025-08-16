%{
#include <stdio.h>
%}


%%
False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield    { printf("Keyword: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*    { printf("Identifier: %s\n", yytext); }
[ \t\n]+                  { /* skip whitespace */ }
.                         { /* skip other characters */ }
%%


int main(void) {
    yylex();
    return 0;
}
int yywrap(void) {
    return 1;
}



