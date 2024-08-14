#!/usr/bin/perl

## SUN BOARD �⏕�v���O����
## �ߋ����O�\���E�����V�X�e��
## sunbbs2.cgi (1999/09/05)
## by KENT

## ----- ��{�ݒ� --------------------- #

$script = './sunbbs2.cgi';		# �X�N���v�g��
$nofile = './pastno.dat';		# �J�E���g�t�@�C����
$bbsfile  = './index.html';		# �f���ւ̖߂��
$method = 'POST';			# method�`�� (POST or GET)
$logfile = './sunbbs.log';		# YY-BOARD���O�t�@�C��
$past_dir = ".";			# �ߋ����O�̃f�B���N�g���i�t���p�X���� / ����j
$past_url = ".";			# �ߋ����O�̂t�q�k�i�t���p�X���� http:// ����j

$bground = "";				# �ǎ��ihttp://����L�q�j
$bgcolor = "#000000";			# �w�i�F
$text    = "#FFFFFF";			# �����F���w��
$link    = "#FFFFCC";			# �����N�F���w��i�������N�j
$vlink   = "#FFFF99";			# �����N�F���w��i�������N�j
$alink   = "#FFFFFF";			# �����N�F���w��i�����N���j

## ----- �ݒ芮�� --------------------- #

## body�^�O���`
if ($bground) {
	$body = "<body background=\"$bground\" bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink>";
} else {
	$body = "<body bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink>";
}

# �ߋ����O�J�E���g�t�@�C����ǂݍ���
open(NUM,"$nofile") || &error("Can't open $nofile");
$count = <NUM>;
close(NUM);


## -------- ���C������ --------------------------------- ##

&get_form;
if (!$buffer) { &frame; }
&form_decode;

if ($mode eq 'ue_html') { &ue_html; }
if ($mode eq 'find_html') { &find_html; }
if ($mode eq 'do_find') { &do_find; }
exit;

## --------- �������� ---------------------------------- ##

## �����������[�`��
sub do_find {
	@lines = ();
	foreach (1 .. $count) {
		open(DB,"$past_dir\/$_\.html");
		@new_data = <DB>;
		close(DB);

		push(@lines,@new_data);
	}

	$word =~ s/�@/ /g;
	$word =~ s/\t/ /g;
	@pairs = split(/ /,$word);

	# �ߋ����O�t�@�C����ǂݍ���
	foreach $line (@lines) {
		$flag = 0;
		foreach $pair (@pairs){
			if (index($line,$pair) >= 0){
				$flag = 1;
				if ($cond eq 'or') { last ; }
			} else {
				if ($cond eq 'and'){ $flag = 0; last; }
			}
		}
		# �q�b�g�����s��V�K�z��(@new)�Ɋi�[
		if ($flag) { push(@new,$line) ; }
	}

	# �������ʂ̔z�񐔂𐔂���
	$count = @new;

	# �Y���Ȃ��̏ꍇ
	if ($count == 0) { &nainai; }

	# ���ʂ��o��
	&header;
	print <<"HTML";
<center><table border=1>
<tr><td>
[<a href="$script?mode=find_html">�� BACK</a>]</td>
<td nowrap>�L�[���[�h <b>$word</b> �� <b>$count</b>��������܂����B
</td></tr></table>
</center><hr>
HTML

	foreach $new_line (@new) {
		($title,$msg) = split(/<\!--T-->/,$new_line);
		print "$title $msg\n";
	}

	print "</body></html>\n";
	exit;
}

## �t���[����
sub frame {
	# �ߋ����O�p�J�E���g�t�@�C�����`�F�b�N
	unless (-e $nofile) { &error("Don't exist $nofile"); }

	print "Content-type: text/html\n\n";
	print "<html>\n<head><title>PastLog</title></head>\n";
	print "<frameset rows=\"110,*\" FRAMEBORDER=no BORDER=0>\n";
	print "<frame name=\"ue\" src=\"$script?mode=ue_html\" target=\"sita\">\n";
	print "<frame name=\"sita\" src=\"$past_url\/$count\.html\">\n";
	print "<noframes>\n";
	print "$body\n";
	print "<center><h3>�t���[���̎g�p�ł��Ȃ����� <a href=\"$script?mode=ue_html\">�������N���b�N</a> ���ĉ������B\n";
	print "</center>\n</body></noframes>\n";
	print "</frameset></html>\n";
	exit;
}

## ��t���[���i���j���[���j
sub ue_html {
	&header;
	print <<"HTML";
<a href="$bbsfile" target="main">�� BBS</a>
<a href="$script?mode=find_html" target="sita">�� Seach</a>
<table width=100%>
<tr><th bgcolor=#0000E8>
<font color=#FFFFFF>Past Log</font>
</th></tr></table>
<hr size=2><center>
[<a href="$past_url\/$count\.html" target="sita"><B>NEW</B></a>]
HTML
	# �ߋ����O��[�����N]��V�K���ɕ\��
	for ($i=$count-1; $i>0; $i--) {
		print "[<a href=\"$past_url\/$i\.html\" target=\"sita\">$i</a>]\n";
	}

	print "</center><hr size=2>\n";
	print "</body></html>\n";
	exit;
}

## �t�H�[���擾
sub get_form {
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }
}

## �t�H�[������̃f�[�^����
sub form_decode {
	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

		$FORM{$name} = $value;
	}
	$word = $FORM{'word'};
	$cond = $FORM{'cond'};
	$mode = $FORM{'mode'};
	$opt  = $FORM{'opt'};
	$chk  = $FORM{'chk'};
}

## �����Y���Ȃ�
sub nainai {
	&header;
	print "<center>������܂���ł����B<hr>\n";
	print "<b>$word</b></center>\n";
	print "</body></html>\n";
	exit;
}

## �����������
sub find_html {
	&header;
	print <<"HTML";
<center>
<table border=0 cellpadding=10>
<tr><td nowrap>
<center><B>�ߋ����O����</B></center>
<OL>
<LI><b>�L�[���[�h</b>����Y���L�����������܂��B
<LI><b>���p�X�y�[�X</b>�ŋ�؂��ĕ����̃L�[���[�h�w�肪��\�\\�ł��B
<LI><b>��������</b>��I�����u��������v�{�^���������ĉ������B
</OL>
</td></tr></table>
<form action="$script" method="$method">
<input type=hidden name=mode value="do_find">
<table border=1>
<tr><td>�L�[���[�h</td><td><input type=text name=word size=30></td></tr>
<tr><td>��������</td><td><input type=radio name=cond value="and" checked>AND
<input type=radio name=cond value="or">OR</td></tr>
<tr><th colspan=2><input type=submit value="��������"></th></tr>
</table>
</form></center>
<hr>
</body></html>
HTML
	exit;
}

## HTML�w�b�_�[��
sub header {
	print "Content-type: text/html\n\n";
	print "<html>\n<head>\n";
	print "<META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=Shift_JIS\">\n";
	print "<title>�ҏW�t�@�C��</title></head>\n";
	print "$body\n";
}

## �G���[����
sub error {
	&header;
	print "<center><hr width=75%><P><h3>ERROR !</h3>\n";
	print "<P><font color=#dd0000><B>$_[0]</B></font>\n";
	print "<P><hr width=75%></center>\n";
	print "</body></html>\n";
	exit;
}

