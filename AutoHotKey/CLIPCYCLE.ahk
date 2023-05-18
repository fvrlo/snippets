%HOTKEY%::
Loop, parse, clipboard, `n, `r,
{
	if(A_LoopField = "")
		break
	; pre-actions
	SendInput %A_LoopField%{enter}
	; post actions
}
return