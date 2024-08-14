#!/usr/bin/perl

## Sun Board v2.3 (1999/09/05) 
## by KENT WEB
## E-MAIL: webmaster@kent-web.com
## WWW: http://www.kent-web.com/

$ver = 'Sun Board v2.3';		# �o�[�W�������i�ҏW�s�v�j

## ---[���ӎ����E���ӎ���]-------------------------------------------------------
## 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B
## 2. ���̃X�N���v�g���g�p���������Ȃ鑹�Q�ɑ΂��č�҂͂��̐ӔC����ؕ����܂���B
## 3. �ݒu�Ɋւ��鎿��͒��ڃ��[���ł͎�t���Ă��܂���̂ŁA�T�|�[�g�f���ւ��肢
##    �������܂��B
## 4. �f�������ɂ��钘�쌠�\�����͐�΂ɍ폜���Ȃ��ŉ������B
## ------------------------------------------------------------------------------

require './jcode.pl';			# �����R�[�h���C�u�����捞

## ----- ��{�ݒ� --------------------- #

$title   = "�ېV��V�E���n�`�I�^�U�E�N���V�b�N";			# �^�C�g����
$t_color = "#000000";			# �^�C�g���̐F
$t_size  = 4;				# �^�C�g���̃T�C�Y
$t_face  = '�l�r �o�S�V�b�N';		# �^�C�g�������̃^�C�v

$bground = "";				# �ǎ� (�p�X�t���Ŏw��j
$bgcolor = "#CCFFFF";			# �w�i�F
$text    = "#333333";			# �����F���w��
$link    = "#663300";			# �����N�F���w��i�������N�j
$vlink   = "#330000";			# �����N�F���w��i�������N�j
$alink   = "#FF0000";			# �����N�F���w��i�����N���j

$pass = '1682';				# �Ǘ��p�p�X���[�h(�p����)
$home = "http://waiwai.ciao.jp/waiwai/index.shtml";		# �߂�� (index.html�Ȃ�)
$max  = 100;				# �L���̍ő�ێ���
$pagelog  = 100;				# �\���t�@�C����1�y�[�W�̋L����
$autolink = 1;				# ���������N (0=no 1=yes)
$log_dir = ".";				# ���O�f�B���N�g�� (�t���p�X���� / ����)
$htm_dir = ".";				# �\���t�@�C���f�B���N�g�� (�t���p�X���� / ����)

# CGI�X�N���v�g���g��URL�Ŏw��
$script  = "http://waiwai.ciao.jp/waiwai/sunbbs/ryoma3/sunbbs.cgi";

# �\���t�@�C�� (index.html) �̂���u�f�B���N�g���v��URL�Ŏw��
$htm_url = "http://waiwai.ciao.jp/waiwai/sunbbs/ryoma3";

## --- ���p�ݒ�
$whatsnew = 1;				# �V�����{�[�h���[�h (0=no 1=yes)
$obi_color = "#663300";			# �薼���̐F
$point  = '��';				# �薼���|�C���^
$point2 = '��';				# �߂�敔�|�C���^
$p_color = "#CC0000";			# �|�C���^�̐F
$s_color = "#FFFFFF";			# �薼�̐F
$t_gif = "";				# �^�C�g��GIF�摜 (http://����L�q)
$tg_w = '250';				# �^�C�g���摜�̕�
$tg_h = '54';				# �^�C�g���摜�̍���
$date_type = 0;				# ���t�̎�� (0=�m�� 1=�a��)
$logfile = "sunbbs.log";		# ���O�t�@�C����
$htmfile = "index.html";		# �\���t�@�C��HTML(��1�y�[�W)
$nexthtm = "index2.html";		# �\���t�@�C��HTML(��2�y�[�W)
$tagkey = 0;				# �f���g�p���̃^�O���� (0=no 1=yes)
$method = 'POST';			# method�`�� (POST/GET)
$lockkey = 0;				# ���b�N�t�@�C������ (0=no 1=symlink 2=open)
$lockfile = './sunbbs.lock';		# ���b�N�t�@�C����
$wrap = 'soft';				# ���s�`�� (soft=�蓮 hard=����)
$nocashe = 1;				# �u���E�U�̃L���b�V���捞������ (0=no 1=yes)
$mailing  = 1;				# ���e������ƃ��[���ʒm����(0=no 1=yes)
$mailto = 'waiwai@bi.ciao.jp';		# ���[���A�h���X(���[���ʒm���鎞)
$sendmail = '/usr/sbin/sendmail';	# sendmail�p�X�i���[���ʒm���鎞�j

## --- �ߋ����O�ݒ� (sunbbs2.cgi �K�{)
$pastkey = 1;				# �ߋ����O�@�\ (0=no 1=yes) 
$past_dir  = ".";			# �ߋ����O�̂���f�B���N�g�� (�t���p�X���� / ����)
$pastno = './pastno.dat';		# �ߋ����O�J�E���g�t�@�C��
$log_line = '150';			# �ߋ����O�P�t�@�C������̍s���̌��x
$subfile = './sunbbs2.cgi';		# �⏕�v���O�����̃t�@�C����

## --- �Ǘ��҃R�����g�i�^�C�g�������ɂ�����Ƃ����R�����g��\���ł��܂��j
$message = <<"MSG";
���g�^��ˑ匀��2006�N11/3�`12/12�E������ˌ���1/2�`2/12
MSG

## --- �X�^�C���V�[�g�ݒ�
$ssheet = 1;				# �X�^�C���V�[�g�̓K�p (0=no 1=yes)
$style = <<"EOM";			# �X�^�C���V�[�g�̃^�O���L�q
<STYLE type="text/css">
<!--
a:link    {font-size: 10pt; text-decoration:none; color:$link; }
a:visited {font-size: 10pt; text-decoration:none; color:$vlink; }
a:active  {font-size: 10pt; text-decoration:none; color:$alink; }
a:hover   {font-size: 10pt; text-decoration:underline; color:$alink; }
-->
</STYLE>
EOM

## ----- �ݒ芮�� --------------------- #

# body�^�O���`
if ($bground) {
   $body = "<body background=\"$bground\" bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink>";
} else {
   $body = "<body bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink>";
}

# HTML�f�B���N�g���w��ōŌ�� / �����Ă�����؂�̂Ă�
$htm_url =~ s/\/$//;

&form_decode;
if ($mode eq 'regist') { &regist; }
if ($mode eq 'form') { &form; }
if ($mode eq 'form2') { &form2; }
if ($mode eq 'find') { &find; }
if ($mode eq 'admin_in') { &admin_in; }
if ($mode eq 'admin' || $mode eq 'delmsg') { &admin; }
if ($mode eq 'edit' || $mode eq 'admin_del') { &edit; }
if ($mode eq 'del') { &msg_del; }
&location;

## --- ���e�t�H�[���P
sub form {
	# �p�X���[�h�`�F�b�N
	if ($whatsnew && $FORM{'pass'} ne "$pass") { &error("�p�X���[�h���Ⴂ�܂��B"); }

	print "Content-type: text/html\n\n";
	print "<html>\n<head><title>$title</title></head>\n";
	print "<frameset rows=\"280\,*\">\n";
	print "<frame name=\"ue\" src=\"$script?mode=form2&pass=$FORM{'pass'}\">\n";
	print "<frame name=\"sita\" src=\"$htm_url/$htmfile#frame\">\n";
	print "<noframes>\n";
	print "$body\n";
	print "<center><font size=4>�t���[�������p�ł��Ȃ��悤�ł��B\n";
	print "<P><a href=\"$script?mode=form2&pass=$FORM{'pass'}\">�������N���b�N</a> ���ĉ������B\n";
	print "</font></center>\n</body></noframes>\n";
	print "</frameset></html>\n";
	exit;
}

## --- ���e�t�H�[���Q
sub form2 {
	# �N�b�L�[���擾
	if ($whatsnew == 1) { &get_cookie; }

	# �t�H�[���T�C�Y���`
	&form_size;

	&header;

	print "<center><form action=\"$script\" method=\"$method\" target=\"main\">\n";
	print "<input type=hidden name=mode value=\"regist\">\n";
	print "<input type=hidden name=pass value=\"$FORM{'pass'}\">\n";

	# �f�����[�h�̂Ƃ�
	if ($whatsnew == 0) {

	  ## -- �ԐM�̏ꍇ
	  if ($FORM{'no'}) {
		# ���O���J��
		open(DB,"$log_dir/$logfile") || &error("Can't open $logfile");
		@lines = <DB>;
		close(DB);

		# �e�L��������������
		foreach $line (@lines) {
			($num,$date,$name,$email,$sub,$com) = split(/<>/,$line);
			if ($FORM{'no'} eq "$num") {
				if ($sub eq "") { $sub = "no title"; }
				last;
			}
		}

		# �ԐM�p���ڂ��쐬
		if ($sub =~ /^Re/) {
			$sub =~ s/Re//;
			$res_sub = "Re\[$num\]" . "$sub";
		} else {
			$res_sub = "Re\[$num\]\: $sub";
		}

		$res_com = "\&gt\; $com";
		$res_com =~ s/<br>/\r\&gt\; /ig;

		print "</center><blockquote>\n";
		print "�ȉ��́A�L��NO <b>[$num] $sub</b> ($name����) �ɑ΂���ԐM�t�H�[���ł��B<hr>\n";
		print "�y�e�L���z<P><table width=90% cellpadding=5 border=1><tr>\n";
		print "<td>$com</td></tr></table>\n";
		print "</blockquote><center>\n";
	  }

	  print "<table border=0>\n";
	  print "<tr><td nowrap><b>���Ȃ܂�</b></td>\n";
	  print "<td><input type=text name=name size=\"$nam_wid\" value=\"$c_name\"></td></tr>\n";
	  print "<tr><td nowrap><b>�d���[��</b></td>\n";
	  print "<td><input type=text name=email size=\"$nam_wid\" value=\"$c_email\"></td></tr>\n";

	# �V���{�[�h���[�h�̂Ƃ�
	} else {
	  print "���e����L�����ȉ��̃t�H�[���ɋL�q���u���e����v�{�^���������ĉ������B<P>\n";
	  print "<table border=1>\n";
	  print "<tr><td nowrap><b>���@�t</b></td>\n";
	  print "<td><input type=text name=date value=\"$date\" size=20></td></tr>\n";
	}

	print "<tr><td nowrap><b>���@�O</b></td>\n";
	print "<td><input type=text name=subj size=\"$sub_wid\" value=\"$res_sub\">\n";
	print "<input type=submit value=\"���e����\">";
	print "<input type=reset value=\"���Z�b�g\"></td></tr>\n";
	print "<tr><td colspan=2><b>�R�����g</b><br>";
	print "<textarea name=comment cols=\"$com_wid\" rows=6 wrap=$wrap>$res_com</textarea></tr>\n";
	print "<tr><td nowrap><b>�t�q�k</b></td>";
	print "<td><input type=text name=url size=$url_wid value=\"http://$c_url\"></td></tr>\n";

	if ($whatsnew == 0) {
	  print "<tr><td nowrap><b>�폜�L�[</b></td>";
	  print "<td><input type=password name=pwd size=8 maxlength=8 value=\"$c_pwd\">\n";
	  print "�����̋L�����폜���Ɏg�p(�p������8�����ȓ�)</td></tr>\n";
	}

	print "</table></form></center>\n";
	print "</body></html>\n";
	exit;
}

## --- �����ݏ���
sub regist {
	# �p�X���[�h�`�F�b�N

	if ($whatsnew && $FORM{'pass'} ne "$pass") { &error("�p�X���[�h���Ⴂ�܂��B"); }

	if ($whatsnew == 0 && $name eq "") { &error("�Ȃ܂��̋L��������܂���B"); }
	if ($comment eq "") { &error("�R�����g�ɋL��������܂���B"); }

	# ���b�N�J�n
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	open(DB,"$log_dir\/$logfile") || &error("Can't open $logfile");
	@lines = <DB>;
	close(DB);

	# ��d���e�̋֎~
	($knum,$kdate,$kname,$kemail,$ksubj,$kcom) = split(/<>/,$lines[0]);
	if ($name eq $kname && $comment eq $kcom) { &error("��d���e�͋֎~�ł�"); }

	# �N�b�L�[�𔭍s
	if ($whatsnew == 1) { &set_cookie; }

	## �ߋ����O���擾����ꍇ
	if ($pastkey && $#lines >= $max-1) { &pastlog; }

	# �L��No�J�E���g
	$number = $knum + 1;

	# �ő�L��������؂�̂�
	$i=0;
	@new = ();
	foreach (0 .. $#lines) {
		push (@new,$lines[$i]);
		$i++;
		if ($i >= $max-1) { last; }
	}

	# �폜�L�[���Í���
	if ($pwd) { &pwd_encode($pwd); }

	# �z�X�g�����擾
	&get_host;

	# ���t����
	if ($whatsnew) { $date = $FORM{'date'}; }

	# ���O���t�H�[�}�b�g
	unshift (@new,"$number<>$date<>$name<>$email<>$subj<>$comment<>$url<>$host<>$ango<>\n");
	# ���O���X�V
	open(DB,">$log_dir\/$logfile") || &error("Can't write $logfile");
	print DB @new;
	close(DB);

	# �S�̂̋L������c��
	if ($pagelog < $#new+1) { $flag=1; }

	# HTML�t�@�C���𐶐��i��P�y�[�W�j
	$write_file = "$htm_dir\/$htmfile";
	&html_regist;

	# HTML�t�@�C���𐶐��i��Q�y�[�W�j
	if ($flag) {
		$write_file = "$htm_dir\/$nexthtm";
		&html_regist;
	}

	# ���b�N����
	unlink($lockfile) if (-e $lockfile);

	# HTML�t�@�C���֖߂�
	&location;

	# ���[���ʒm����
	if ($mailing && $email ne "$mailto") { &mail_to; }

	exit;
}

## --- HTML��������
sub html_regist {
	open(HTML,">$write_file") || &error("Can't write $write_file");

	# HTML�w�b�_��
	print HTML "<html>\n<head>\n";
	print HTML "<META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=Shift_JIS\">\n";
	print HTML "<title>$title</title>\n";

	# �X�^�C���V�[�g�K�p
	if ($ssheet) { print HTML "$style\n"; }

	# �L���b�V���捞����
	if ($nocashe) { print HTML "<META HTTP-EQUIV=\"Pragma\" CONTENT=\"no-cache\">\n"; }

	print HTML "</head>\n";
	print HTML "$body\n";

	# �����N��
	print HTML "<B><font color=$p_color>$point2</font>";
	print HTML "<a href=\"$home\" target=\"_top\">HomePage</a>\n";

	if ($whatsnew == 0) {
	  print HTML "<font color=$p_color>$point</font>";
	  print HTML "<a href=\"$script?mode=form\">PostMessage</a>\n";
	}

	print HTML "<font color=$p_color>$point</font>";
	print HTML "<a href=\"$script?mode=find\">Search</a>\n";

	# �ߋ����O
	if ($pastkey) {
	  print HTML "<font color=$p_color>$point</font>";
	  print HTML "<a href=\"$subfile\">PastLog</a>\n";
	}

	print HTML "<font color=$p_color>$point</font>";
	print HTML "<a href=\"$script?mode=admin_in\">Admin</a>\n";
	print HTML "</B>\n<center>\n<P>\n";

	# �^�C�g����
	if ($t_gif eq '') {
	  print HTML "<font color=\"$t_color\" size=\"$t_size\" face=\"$t_face\"><b>$title</b></font>\n";
	} else {
	  print HTML "<img src=\"$t_gif\" width=$tg_w height=$tg_h>\n";
	}

	# �ЂƂ��ƃ��b�Z�[�W��\��
	$message =~ s/\r\n/<br>/g;
	$message =~ s/\r/<br>/g;
	$message =~ s/\n/<br>/g;

	print HTML "<P>$message</center>\n";
	print HTML "<hr><a name=\"frame\"></a>\n";

	# �L�������`
	if ($flag == 2) { $start = $pagelog; $end = $#new; }
	else {
	  $start = 0;
	  if ($i < $pagelog) { $end = $i; }
	  else { $end = $pagelog-1; }
	}

	# �L����W�J
	foreach ($start .. $end) {
	  local($num,$date,$name,$email,$sub,$com,$url,$host) = split(/<>/,$new[$_]);

	  if ($sub eq "") { $sub = "no title"; }
	  if ($autolink) { &auto_link($com); }

	  # �f�����[�h�̏ꍇ
	  if ($whatsnew == 0) {
		print HTML "<table border=0 width=100% cellpadding=1><tr>\n";
		print HTML "<td bgcolor=$obi_color> <font color=$p_color>$point</font>\n";
		print HTML "<font color=$s_color size=3><b>$sub</b></font></td>\n";
		print HTML "</tr></table>\n";
		print HTML "<table cellspacing=0 cellpadding=0 width=95% align=center>\n";
		print HTML "<tr><td>No.</td><td>�F<B>$num</B></td>";
		print HTML "<td></td><td></td></tr>\n";
		print HTML "<tr><td>Name</td><td>�F<b>$name</b></td>";
		print HTML "<td></td><td></td></tr>\n";
		print HTML "<tr><td>Date</td><td>�F$date</td>";
		print HTML "<td></td><td></td></tr>\n";

		# ���[���\��
		if ($email) {
		    print HTML "<tr><td>Mail</td><td>�F<a href=mailto:$email>$email</a></td>";
		    print HTML "<td></td><td></td></tr>\n";
		}

		# URL�\��
		if ($url) {
		    print HTML "<tr><td>URL</td><td>�F<a href=http://$url target=_top>http://$url</a></td>";
		    print HTML "<td></td><td></td></tr>\n";
		}

		print HTML "<tr><td></td><td width=100% colspan=3><br>$com</td>\n";
		print HTML "<td align=right valign=bottom>\n";
		print HTML "<form action=\"$script\" method=$method>\n";
		print HTML "<input type=hidden name=mode value=\"form2\">\n";
		print HTML "<input type=hidden name=no value=\"$num\">\n";
		print HTML "<input type=submit value=\"�ԐM\"></form>\n";
		print HTML "</td></tr></table><P>\n";

	  # �V���{�[�h���[�h�̏ꍇ
	  } else {
		print HTML "<table border=0 width=100% cellpadding=2><tr>\n";
		print HTML "<td bgcolor=$obi_color> <font color=$p_color>$point</font>\n";
		print HTML "<font color=$s_color size=3><b>$sub</b></font></td>\n";
		print HTML "</tr></table>\n";
		print HTML "<table><tr><td width=15>�@</td>\n";
		print HTML "<td>Date: $date</td></tr></table>\n";
		print HTML "<P><blockquote>$com\n";

		if ($url) {
		    print HTML "<P><a href=\"http://$url\" target=_top>http://$url</a>\n";
		}

		print HTML "</blockquote>\n";
	  }

	  print HTML "<hr>\n";

	} ## foreach -- END

	if ($whatsnew == 0) {
	    print HTML "<Table width=100% Border=0><Tr><Td>\n";
	}

	# ���^�O�y�[�W�̃����N�𐶐�
	if ($flag == 1) {
	  print HTML "<form action=\"$htm_url/$nexthtm\">";
	  print HTML "<input type=submit value=\"���y�[�W\"></form></td><td>\n";
	  $flag=2;

	} elsif ($flag == 2) {
	  print HTML "<form action=\"$htm_url/$htmfile\">";
	  print HTML "<input type=submit value=\"�O�y�[�W\"></form></Td><Td>\n";
	}

	# �폜�t�H�[��
	if ($whatsnew == 0) {
	  print HTML "<form action=\"$script\" method=\"$method\">\n";
	  print HTML "<div align=right><table><tr><td>\n";
	  print HTML "<font color=$t_color>�ȉ��̃t�H�[�����玩���̋L�����폜�ł��܂�</font><br>\n";
	  print HTML "�L��No <input type=text name=no size=4>\n";
	  print HTML "�폜�L�[ <input type=password name=pwd size=4>\n";
	  print HTML "<input type=hidden name=mode value=\"del\">\n";
	  print HTML "<input type=submit value=\"�폜����\"></td></tr></table></div>\n";
	  print HTML "</Td></Tr></Table></form>\n";
	}

	# ���쌠��\���i�폜�֎~�j
	print HTML "<center><small><!-- $ver -->\n";
	print HTML "- <a href=\"http://www.kent-web.com/\" target=_top>Sun Board</a> -\n";
	print HTML "</small></center>\n";
	print HTML "</body></html>\n";
	close(HTML);
}

## --- �\���t�@�C���ɃW�����v
sub location {
	# IIS�T�[�o�Ή�
	if ($ENV{PERLXS} eq "PerlIS") {
		print "HTTP/1.0 302 Temporary Redirection\r\n";
		print "Content-type: text/html\n";
	}
	print "Location: $htm_url\/$htmfile\n\n";
}

## --- �Ǘ����[�h�������
sub admin_in {
	&header;
	print "<table width=100%><tr><th bgcolor=$obi_color>\n";
	print "<font color=$s_color>�p�X���[�h�m�F���</font></th></tr></table>\n";
	print "<P><center><B>�p�X���[�h����͂��ĉ������B</B>\n";
	print "<form action=\"$script\" method=\"$method\">\n";

	# �V�����{�[�h���͑I���{�^����\��
	if ($whatsnew) {
		print "<input type=radio name=mode value=\"form\" checked><B>�L������</B>\n";
	}
	else {
		print "<input type=hidden name=mode value=\"admin\">\n";
	}

	print "<input type=password name=pass size=10>";
	print "<input type=submit value=\" �F�� \"></form>\n";
	print "</center>\n</body>\n</html>\n";
	exit;
}

## --- �Ǘ��p�������
sub admin {
	# �p�X���[�h�`�F�b�N
	if ($FORM{'pass'} ne "$pass") { &error("�p�X���[�h���Ⴂ�܂��B"); }

	# ���O�t�@�C�����J��
	open(DB,"$log_dir\/$logfile") || &error("Can't open $logfile");
	@lines = <DB>;
	close(DB);

	&header;
	print "[<a href=\"$htm_url/$htmfile\">�f���ւ��ǂ�</a>]\n";
	print "<table width=100%><tr><th bgcolor=$obi_color>\n";
	print "<font color=$s_color>�� �� �� ��</font></th></tr></table>\n";

	# �L���ҏW���
	if ($FORM{'edit'}) {

	&form_size;

	foreach $line (@lines) {
		($num,$date,$name,$email,$subj,$com,$url,$host) = split(/<>/,$line);
		if ($FORM{'edit'} eq "$num") { last; }
	}

	$com =~ s/<br>/\r/g;
	if ($url) { $url = "http://$url"; }

	print <<"EOM";
<P><center><h4>�ҏW���镔���̂ݏ��������A�ҏW�{�^���������ĉ������B</h4>
<P><form action="$script" method="$method">
<input type=hidden name=pass value="$FORM{'pass'}">
<input type=hidden name=mode value="edit">
<input type=hidden name=edit value="$num">
<table border=0>
EOM
	if ($whatsnew == 0) {
	  print "<tr><td nowrap><b>���Ȃ܂�</b></td>";
	  print "<td><input type=text name=name size=$nam_wid value=\"$name\"></td></tr>\n";
	  print "<tr><td nowrap><b>�d���[��</b></td>";
	  print "<td><input type=text name=email size=$nam_wid value=\"$email\"></td></tr>\n";
	}

	print "<tr><td nowrap><b>�^�C�g��</b></td>";
	print "<td><input type=text name=subj size=\"$sub_wid\" value=\"$subj\"></td></tr>\n";
	print "<tr><td colspan=2><b>�R�����g</b><br>";
	print "<textarea name=comment cols=$com_wid rows=6 wrap=$wrap>$com</textarea></tr>\n";
	print "<tr><td nowrap><b>�t�q�k</b></td>";
	print "<td><input type=text name=url size=\"$url_wid\" value=\"$url\"></td></tr>\n";
	print "<tr><th colspan=2>\n";
	print "<input type=submit value=\"�L����ҏW����\">";
	print "<input type=reset value=\"���Z�b�g\"></th></tr></table>\n";
	}

	# �Ǘ��p�������
	else {

		print <<"EOM";
<P><center>
<table><tr><td>
  <UL>
  <LI>�L�����폜����ꍇ�̓`�F�b�N�{�b�N�X�Ƀ`�F�b�N�����A�폜�{�^���������ĉ������B
  <LI>�L����ҏW����ꍇ�́A<B>No.</B> ���N���b�N����ƕҏW��ʂƂȂ�܂��B
  </UL>
</td></tr></table>
<P><form action="$script" method="$method">
<input type=hidden name=pass value="$FORM{'pass'}">
<input type=hidden name=mode value="admin_del">
<input type=submit value="�L�����폜����"><input type=reset value="���Z�b�g"><P>
<table border=1>
<tr><th>�폜</th><th>����</th><th>No.</th><th>�^�C�g��</th>
EOM

	if ($whatsnew == 0) {
		print "<th>�Ȃ܂�</th><th>�z�X�g</th>";
	}

	print "<th>�R�����g</th></tr>\n";

	foreach $line (@lines) {
		($num,$date,$name,$email,$subj,$com,$url,$host) = split(/<>/,$line);

		if ($email) { $name = "<a href=\"mailto:$email\">$name</a>"; }
		if (!$subj) { $subj = "no title"; }

		$com =~ s/<br>/ /ig;
		$com =~ s/</\&lt\;/g; $com =~ s/>/\&gt\;/g;
		if (length($com) > 60) { $com = substr($com,0,58); $com = $com . '..'; }

		print "<tr><th><input type=checkbox name=del value=\"$num\"></th>";
		print "<td><small>$date</small></td>";
		print "<th><a href=\"$script?mode=admin&edit=$num&pass=$FORM{'pass'}\">$num</a></th>";
		print "<td><small><b>$subj</b></small></td>";

		if ($whatsnew == 0) {
			print "<th>$name</th><td><small>$host</small></td>\n";
		}

		print "<td><small>$com</small></td></tr>\n";
	}

	print "</table></form></center>\n";
	}

	print "</body>\n</html>\n";
	exit;
}

## --- �L���폜�^�ҏW����
sub edit {
	# �p�X���[�h�`�F�b�N
	if ($FORM{'pass'} ne "$pass") { &error("�p�X���[�h���Ⴂ�܂��B"); }

	# ���b�N�J�n
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	# ���O�t�@�C�����J��
	open(DB,"$log_dir\/$logfile") || &error("Can't open $logfile");
	@lines = <DB>;
	close(DB);

	if ($mode eq 'admin_del') {
		@new=();
		foreach $line (@lines) {
			local($flag) = 0;
			($num,$date,$name,$email,$subj,$com,$url,$host,$pwd)
								 = split(/<>/,$line);
			foreach $delno (@delnos) {
				if ($delno eq "$num") { $flag=1; last; }
			}
			if ($flag == 0) { push(@new,$line); }
		}

	} else {
		$FORM{'url'} =~ s/^http\:\/\///;
		# �Y���L���𔲂��o���č����ւ�
		@new = ();
		foreach $line (@lines) {
		  ($num,$date,$name,$email,$subj,$com,$url,$host,$pwd) = split(/<>/,$line);
		  if ($FORM{'edit'} ne "$num") { push(@new,$line); }
		  else { push(@new,"$num<>$date<>$FORM{'name'}<>$FORM{'email'}<>$FORM{'subj'}<>$comment<>$FORM{'url'}<>$host<>$pwd<>\n"); }
		}
	}

	# ���O�t�@�C�����㏑��
	open(DB,">$log_dir\/$logfile") || &error("Can't write $logfile");
	print DB @new;
	close(DB);

	# �S�̂̋L������c��
	if ($pagelog < $#new+1) { $flag=1; }

	# HTML�t�@�C���𐶐��i��P�y�[�W�j
	$i = $#new;
	$write_file = "$htm_dir\/$htmfile";
	&html_regist;

	# HTML�t�@�C���𐶐��i��Q�y�[�W�j
	if ($flag) { $write_file = "$htm_dir\/$nexthtm"; &html_regist; }

	# ���b�N����
	unlink($lockfile) if (-e $lockfile);

	# �폜������͊Ǘ���ʂɖ߂�
	if ($mode eq "admin_del") { &admin; }

	# �ҏW������͌f���֖߂�
	else {
		# �\���t�@�C���ɖ߂�
		&location;
		exit;
	}
}

## --- �L���폜����
sub msg_del {
	# �t�H�[���`�F�b�N
	if ($FORM{'no'} eq "") { &error("�L��NO�����͂���Ă��܂���B"); }
	if ($FORM{'pwd'} eq "") { &error("�폜�L�[�����͂���Ă��܂���B"); }

	# ���b�N�J�n
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	# ���O�t�@�C�����J��
	open(DB,"$log_dir\/$logfile") || &error("Can't open $logfile");
	@lines = <DB>;
	close(DB);

	# ���O�𕪉����A�폜�L��������
	$hit=0;
	foreach $line (@lines) {
		$del=0;
		($num,$date,$name,$email,$sub,$com,$url,$host,$lpwd) = split(/<>/,$line);
		if ($FORM{'no'} eq "$num") {
			$del=1; $hit=1;
			$delkey = $lpwd;
		}
		push(@new,$line) if ($del == 0);
	}
	if ($hit == 0) { &error("�Y���̋L��NO����������܂���B"); }
	if ($delkey eq '') { &error("�폜�L�[���ݒ肳��Ă��܂���B"); }

	# �폜�L�[�ƍ�����
	$del_flag = 0;
	if ($pwd eq "$pass") { $del_flag = 1; }
	else {
		&pwd_decode($delkey);
		if ($check eq 'yes') { $del_flag = 1; }
	}

	if ($del_flag == 0) { &error("�폜�L�[���Ⴂ�܂��B"); }

	# ���O���X�V
	open(DB,">$log_dir\/$logfile") || &error("Can't write $logfile");
	print DB @new;
	close(DB);

	# �S�̂̋L������c��
	if ($pagelog < $#new+1) { $flag=1; }

	# HTML�t�@�C���𐶐��i��P�y�[�W�j
	$i = $#new;
	$write_file = "$htm_dir\/$htmfile";
	&html_regist;

	# HTML�t�@�C���𐶐��i��Q�y�[�W�j
	if ($flag) { $write_file = "$htm_dir\/$nexthtm"; &html_regist; }

	# ���b�N����
	unlink($lockfile) if (-e $lockfile);

	# ������ʂɖ߂�
	&location;
	exit;
}

## --- �t�H�[������̃f�[�^����
sub form_decode {
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		if ($ENV{'CONTENT_LENGTH'} > 51200) { &error("���e�ʂ��傫�����܂��B"); }
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }

	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

		# �����R�[�h�ϊ�
		&jcode'convert(*value,'sjis');

		# �^�O����
		if ($whatsnew == 0 && $tagkey == 0) {
			$value =~ s/&/&amp\;/g;
			$value =~ s/</&lt\;/g;
			$value =~ s/>/&gt\;/g;
		} else {
			$value =~ s/<!--(.|\n)*-->//g;
			$value =~ s/<>/&lt\;&gt\;/g;
		}

		# �폜����
		if ($name eq "del") { push(@delnos,$value); }

		$FORM{$name} = $value;
	}
	$name    = $FORM{'name'};
	$comment = $FORM{'comment'};
	$comment =~ s/\r\n/<br>/g;
	$comment =~ s/\r/<br>/g;
	$comment =~ s/\n/<br>/g;
	$email   = $FORM{'email'};
	$url     = $FORM{'url'};
	$url     =~ s/^http\:\/\///;
	$mode    = $FORM{'mode'};
	$pwd     = $FORM{'pwd'};
	$subj    = $FORM{'subj'};

	# �����̎擾
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
	$year += 1900;
	$mon++;
	if ($mon  < 10) { $mon  = "0$mon";  }
	if ($mday < 10) { $mday = "0$mday"; }
	if ($hour < 10) { $hour = "0$hour"; }
	if ($min  < 10) { $min  = "0$min";  }

	# �����̃t�H�[�}�b�g
	if ($date_type) {
		$youbi = ('��','��','��','��','��','��','�y') [$wday];
		if ($whatsnew) {
			$date = "$year�N$mon��$mday�� ($youbi)";
		} else {
			$date = "$year�N$mon��$mday�� ($youbi) $hour��$min��";
		}
	}
	else {
		$youbi = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') [$wday];
		if ($whatsnew) {
			$date = "$year-$mon-$mday ($youbi)";
		} else {
			$date = "$year/$mon/$mday($youbi) $hour\:$min";
		}
	}
}

## --- �G���[����
sub error {
	unlink($lockfile) if (-e $lockfile);

	&header;
	print "<center><hr width=75%><h3>ERROR !</h3>\n";
	print "<P><font color=$t_color><B>$_[0]</B></font>\n";
	print "<P><hr width=75%></center>\n";
	print "</body></html>\n";
	exit;
}

## --- �N�b�L�[�̔��s
sub set_cookie { 
	($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg)
				= gmtime(time + 60*24*60*60);
	$yearg += 1900;
	if ($secg  < 10)  { $secg  = "0$secg";  }
	if ($ming  < 10)  { $ming  = "0$ming";  }
	if ($hourg < 10)  { $hourg = "0$hourg"; }
	if ($mdayg < 10)  { $mdayg = "0$mdayg"; }

	$mong = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
					'Sep','Oct','Nov','Dec') [$mong];
	$youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday',
						'Friday','Saturday') [$wdayg];
	$date_gmt = "$youbi, $mdayg\-$mong\-$yearg $hourg:$ming:$secg GMT";
	$cook="name\:$name\,email\:$email\,url\:$url\,pwd\:$pwd";
	print "Set-Cookie: SUNBBS=$cook; expires=$date_gmt\n";
}

## --- �N�b�L�[���擾
sub get_cookie { 
	@pairs = split(/;/, $ENV{'HTTP_COOKIE'});
	foreach $pair (@pairs) {
		local($name, $value) = split(/=/, $pair);
		$name =~ s/ //g;
		$DUMMY{$name} = $value;
	}
	@pairs = split(/,/, $DUMMY{'SUNBBS'});
	foreach $pair (@pairs) {
		local($name, $value) = split(/:/, $pair);
		$COOKIE{$name} = $value;
	}
	$c_name  = $COOKIE{'name'};
	$c_email = $COOKIE{'email'};
	$c_url   = $COOKIE{'url'};
	$c_pwd   = $COOKIE{'pwd'};

	if ($FORM{'name'}) { $c_name = $FORM{'name'}; }
	if ($FORM{'email'}) { $c_email = $FORM{'email'}; }
	if ($FORM{'url'}) { $c_url = $url; }
	if ($FORM{'pwd'}) { $c_pwd = $FORM{'pwd'}; }
}

## --- ���[�h�����T�u���[�`��
sub find {
	&header;

	print <<"HTML";
[<a href="$htm_url/$htmfile">�f���ɂ��ǂ�</a>]
<table width=100%>
<tr>
  <th bgcolor="$obi_color">
    <font color="$s_color">���[�h����</font>
  </th>
</tr>
</table>
<P><center>
<table>
<tr>
  <td>
    ������������<b>�L�[���[�h</b>����͂��A����������I�����u��������v�������Ă��������B<br>
    �������̃L�[���[�h����͂���Ƃ��́A<b>���p�X�y�[�X</b>�ŋ�؂��ĉ������B
  </td>
</tr>
</table>
<P><form action="$script" method="$method">
<input type=hidden name=mode value="find">
<table border=1>
<tr>
  <th colspan=2>�L�[���[�h <input type=text name=word size=30></th>
</tr>
<tr>
  <td>��������</td>
  <td>
    <input type=radio name=cond value="and" checked>AND
    <input type=radio name=cond value="or">OR
  </td>
</tr>
<tr>
  <th colspan=2>
    <input type=submit value="��������"><input type=reset value="���Z�b�g">
  </th>
</tr>
</table>
</form></center>
HTML
	# ���[�h�����̎��s�ƌ��ʕ\��
	if ($FORM{'word'} ne "") {

		# ���͓��e�𐮗�
		$cond = $FORM{'cond'};
		$word = $FORM{'word'};
		$word =~ s/�@/ /g;
		$word =~ s/\t/ /g;
		@pairs = split(/ /,$word);

		# �t�@�C����ǂݍ���
		open(DB,"$log_dir/$logfile") || &error("Can't open $logfile");
		@lines = <DB>;
		close(DB);

		# ��������
		foreach $line (@lines) {
			$flag = 0;
			foreach $pair (@pairs){
				if (index($line,$pair) >= 0){
					$flag = 1;
					if ($cond eq 'or') { last; }
				} else {
					if ($cond eq 'and'){ $flag = 0; last; }
				}
			}
			if ($flag == 1) { push(@new,$line); }
		}

		# �����I��
		$count = @new;
		print "<hr><b><font color=$t_color>�������ʁF$count��</font></b><P>\n";
		print "<OL>\n";

		foreach $line (@new) {
		  ($no,$date,$name,$email,$sub,$com,$url) = split(/<>/,$line);
		  if (!$sub) { $sub = "����"; }
		  if ($email) { $name = "<a href=mailto:$email>$name</a>"; }
		  if ($url) { $url = "<a href=http://$url target=_top>http://$url</a>"; }

		  # ���ʂ�\��
		  print "<LI>[$no] <font color=$t_color><b>$sub</b></font>\n";
		  print "���e�ҁF<b>$name</b> <small>���e���F$date</small>\n";
		  print "<P><blockquote>$com<P>$url</blockquote><hr>\n";
		}

		print "</OL>\n";
	}
	print "</body></html>\n";
	exit;
}

## --- �u���E�U�𔻒f���t�H�[�����𒲐�
sub form_size {
	# �u���E�U�����擾
	$agent = $ENV{'HTTP_USER_AGENT'};

	# MSIE 3 �̏ꍇ
	if ($agent =~ /MSIE 3/i) {
		$nam_wid = 30;
		$sub_wid = 40;
		$com_wid = 65;
		$url_wid = 48;
	}
	# MSIE 4/5 �̏ꍇ
	elsif ($agent =~ /MSIE 4/i || $agent =~ /MSIE 5/i) {
		$nam_wid = 30;
		$sub_wid = 40;
		$com_wid = 65;
		$url_wid = 78;
	}
	# ���̑�
	else {
		$nam_wid = 20;
		$sub_wid = 25;
		$com_wid = 56;
		$url_wid = 50;
	}
}

## --- HTML�̃w�b�_�[
sub header { 
	print "Content-type: text/html\n\n";
	print "<html>\n<head>\n";

	# �X�^�C���V�[�g
	if ($ssheet) { print "$style\n"; }

	# �L���b�V���捞����
	if ($nocashe) { print "<META HTTP-EQUIV=\"Pragma\" CONTENT=\"no-cache\">\n"; }

	print "<META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=x-sjis\">\n";
	print "<title>$title</title></head>\n";
	print "$body\n";
}

## --- �p�X���[�h�Í�����
sub pwd_encode {
	$now = time;
	($p1, $p2) = unpack("C2", $now);
	$wk = $now / (60*60*24*7) + $p1 + $p2 - 8;
	@saltset = ('a'..'z','A'..'Z','0'..'9','.','/');
	$nsalt = $saltset[$wk % 64] . $saltset[$now % 64];
	$ango = crypt($_[0], $nsalt);
}

## --- �p�X���[�h�ƍ�����
sub pwd_decode {
	if ($_[0] =~ /^\$1\$/) { $crptkey = 3; } # FreeBSD�T�[�o�Ή�
	else { $crptkey = 0; }
	$check = "no";
	if (crypt($FORM{'pwd'}, substr($_[0],$crptkey,2)) eq "$_[0]") {
		$check = "yes";
	}
}

## --- ���b�N�t�@�C���isymlink�֐��j
sub lock1 { 
	local($retry) = 5;
	while (!symlink(".", $lockfile)) {
		if (--$retry <= 0) { &error("LOCK is BUSY"); }
		sleep(1);
	}
}

## --- ���b�N�t�@�C���iopen�֐��j
sub lock2 {
	local($flag) = 0;
	foreach (1 .. 5) {
		unless (-e $lockfile) {
			open(LOCK,">$lockfile");
			close(LOCK);
			$flag = 1;
			last;
		} else {
			sleep(1);
		}
	}
	if ($flag == 0) { &error("LOCK is BUSY"); }
}

## --- �z�X�g�����擾
sub get_host {
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq "" || $host eq "$addr") {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
	}
	if ($host eq "") { $host = $addr; }
}

## --- ���������N
sub auto_link {
	$_[0] =~ s/([^=^\"]|^)(http\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#]+)/$1<a href=$2 target=_top>$2<\/a>/g;
}

## --- ���[�����M
sub mail_to {
	# ���M���e�� JIS�R�[�h�ϊ�
    	&jcode'convert(*title,'jis');
    	&jcode'convert(*name,'jis');
    	&jcode'convert(*subj,'jis');
    	&jcode'convert(*comment,'jis');
	if ($date_type == 1) { &jcode'convert(*date,'jis'); }

	# �R�����g�{���̉��s�𕜌�
	$comment =~ s/<br>/\n/ig;
	$comment =~ s/&lt;/</g;
	$comment =~ s/&gt;/>/g;

	# sendmail�N��
	if (open(MAIL,"| $sendmail $mailto")) {
	print MAIL "To: $mailto\n";

	# ���[���A�h���X���Ȃ��ꍇ�̓_�~�[���[���ɒu������
	if ($email eq "") { $email = 'nomail@xxx.xxx'; }

	print MAIL "From: $email\n";
	print MAIL "Subject: $title [$subj]\n";
	print MAIL "Content-type: text/plain; charset=ISO-2022-JP\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	print MAIL "TIME : $date\n";
	print MAIL "HOST : $host\n";
	print MAIL "NAME : $name\n";
	print MAIL "MAIL : $email\n";

	if ($url) { print MAIL "URL  : http://$url\n"; }
	if (!$subj) { $subj = "no title"; }

	print MAIL "TITLE: $subj\n\n";
	print MAIL "$comment\n";
	close(MAIL);
	}
}

## --- �ߋ����O����
sub pastlog {
	$new_flag = 0;

	open(NUM,"$pastno") || &error("Can't open $pastno");
	$count = <NUM>;
	close(NUM);

	# �ߋ����O�̃t�@�C�������`
	$pastfile  = "$past_dir\/$count\.html";

	# �ߋ����O���Ȃ��ꍇ�A�V�K�Ɏ�����������
	unless(-e $pastfile) { &new_log; }

	if ($new_flag == 0) {
		open (DB,"$pastfile") || &error("Can't open $pastfile");
		@past = <DB>;
		close(DB);
	}

	# �K��̍s�����I�[�o�[����ƁA���t�@�C����������������
	if ($#past > $log_line) { &next_log; }

	$pst_line = $lines[$max-1];
	$pst_line =~ s/\n//g;

	($pnum,$pdate,$pname,$pemail,$psub,$pcom,$purl,$phost) = split(/<>/, $pst_line);
	if (!$psub) { $psub = "����"; }
	if ($pemail) { $pname = "<a href=\"mailto\:$pemail\">$pname</a>"; }
	if ($purl) { $purl = "<a href=http://$purl target=_top>http://$purl</a>"; }

	# ���������N
	if ($autolink) { &auto_link($pcom); }

	# �L���̃��C�A�E�g
	$html = <<"HTML";
[$pnum] <font color=$t_color><b>$psub</b></font> <b>$pname</b> <small>$pdate</small><P><blockquote>$pcom<P>$purl</blockquote><!--$phost--><hr>
HTML

@news = ();
foreach $line (@past) {
	if ($line =~ /<!--OWARI-->/i) { last; }
	push (@news,$line);
	if ($line =~ /<!--HAJIME-->/i) { push (@news,"$html"); }
}

push (@news,"<!--OWARI-->\n</body></html>\n");

open(DB,">$pastfile") || &error("Can't write $pastfile");
print DB @news;
close(DB);

}## --- �ߋ����O���� --- ##

## --- �ߋ����O���t�@�C���������[�`��
sub next_log {
	# ���t�@�C���̂��߂̃J�E���g�A�b�v
	$count++;

	# �J�E���g�t�@�C���X�V
	open(NUM,">$pastno") || &error("Can't write $pastno");
	print NUM "$count";
	close(NUM);

	$pastfile  = "$past_dir\/$count\.html";

	&new_log;
}

## --- �V�K�ߋ����O�t�@�C���������[�`��
sub new_log {
	$new_flag = 1;

	$past[0] = "<html><head><title>�ߋ����O</title></head>\n";
	$past[1] = "<body background=\"$bground\" bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink><hr size=2>\n";
	$past[2] = "<\!--HAJIME-->\n";
	$past[3] = "<\!--OWARI-->\n";
	$past[4] = "</body></html>\n";

	# �V�K�ߋ����O�t�@�C���𐶐��X�V
	open(DB,">$pastfile") || &error("Can't write $pastfile");
	print DB @past;
	close(DB);

	# �p�[�~�b�V������666�ցB
	chmod(0666,"$pastfile");
}
