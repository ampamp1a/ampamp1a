   M S B A M L   `   `   `  ????E  ATicTacToe3, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null%clr-namespace:TicTacToe	TicTacToe  5   	       TicTacToe.MainWindow   5   	   W SPresentationCore, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5   	   R NSystem.Xaml, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   )localclr-namespace:TicTacToe     5   	     ? Title$  Tic-Tac-Toe??5   	   $	??450??6   $	??800??6*   $??Segoe UI Light)?5	   	      BackgroundColor#??[  5
   	    ? WindowStartupLocation$ CenterScreen=?5   	   .??5      (? .??5   
   ? $
??1168??6    ? ShowGridLines$ False??6    J? RenderTransformOrigin$ 0.544,0.502&?62    ? RowDefinitions 5      ?? 5      $
??auto ?6    ?? 5      $??* ?6    .+?5      ?? -   5         ??Name$ 	TextInput??5      $	??137??5      $??50??5      $
??Left=?5      $??
934,77,0,0q?5      $??1??5       ?? TextWrapping$
 Wrap=?5      $	??Top=?5      $??20(?6)    ?? TextAlignment$ Center=?67   ?? 5      -   5        $
??Play??5        ButtonColor#??[ 5      $??24(?5      $
??Left=?5      $??1084,77,0,0q?5      $??1??6*   $	??Top=?5      $??50??5       $??50??6    6,   ?? 5!      -   5        $??SaveGame??5!      #??[ 5"      $??34(?5#      $	??200??5$      $??0,0,0,5q?5%      
???   ?$??934,171,34,282q?5'   .   $??1??6F   ?? 5(      -   5        $??LoadGame??5(      #??[ 5)      $??34(?5*      $	??200??5+      $??0,0,0,5q?5,      
???   ?$??934,286,34,167q?5.   .   $??1??6F   ?? 5/      -   5         ??Name$ 	TurnPanel??5/      	 ?? Orientation$	 
Horizontal=?50      $??Center=?51      .+?52      ?? $??54(?6   $??Player:??53      $??0,0,0,15q?54      ?? 55      -   5        
 ??Name$
 PlayerImage??55      $??Asset/X15.png??56      $??75??57      58      ? 5:      -   5         ?Name$ TheGrid??5:      $	??500??6$   $	??500??60   $??1??6=   $
 True??6K    ? ColumnDefinitions 5;       5=      5?      ?? 5A      -   5         ??Name$ 
GameCanvas??5A      $??1??5B      $??0??5C      $	??500??5D      $	??500??5E      $??20q?5F      .+?5G      A? -	   5         A?Name$ GameGrid??5G      $	??500??5H      $	??500??5I      ??5K      ?? 5L       ?? 
StartPoint$	 0,0&?6.    ?? EndPoint$	 1,1&?6?   .??5M      ?  ? Color$ 	#00D2D6C1??6+    ? Offset$ 1Q?6=   5N      5Q      ?? 5S      -
   5         ??Name$
 Line??5S        	LineColor#??[ 5T      $??10??5U       ?? StrokeStartLineCap$ Round=?5V       ?? StrokeEndLineCap$ Round=?5W      $y?Hidden=?5X      5Y      ? 5[      -   5        $ 	EndScreen??5[      $??2??5\      #??[  5]      $y?Hidden=?5^      .+?5`      ?? $	 Vertical=?6   $??Center=?5a      .+?5b      ?? $	 
Horizontal=?6!   $??Center=?5c   !   .+?5d      ?? -   5         ??Name$ 
ResultText??5d   $   $??54(?5e   $   $??Winner: ??5f   $   $??0,0,0,15q?5g   $   ?? 5h      -   5        $
 WinnerImage??5h       $??75??5i       $??Asset/X15.png??5j       5k      ?? 5m      -   5        $??
Play Again??5m      #??[ 5n      $??34(?5o      $	??200??5p      $??0,20,0,0q?5q      $??0,0,0,5q?5r      
???   ?5t      5u      5v      5w      5x      5z      