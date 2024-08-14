#!/usr/bin/perl

## Sun Board v2.3 (1999/09/05) 
## by KENT WEB
## E-MAIL: webmaster@kent-web.com
## WWW: http://www.kent-web.com/

$ver = 'Sun Board v2.3';		# バージョン情報（編集不要）

## ---[注意事項・合意事項]-------------------------------------------------------
## 1. このスクリプトはフリーソフトです。
## 2. このスクリプトを使用したいかなる損害に対して作者はその責任を一切負いません。
## 3. 設置に関する質問は直接メールでは受付けていませんので、サポート掲示板へお願い
##    いたします。
## 4. 掲示板下部にある著作権表示部は絶対に削除しないで下さい。
## ------------------------------------------------------------------------------

require './jcode.pl';			# 文字コードライブラリ取込

## ----- 基本設定 --------------------- #

$title   = "維新回天・竜馬伝！／ザ・クラシック";			# タイトル名
$t_color = "#000000";			# タイトルの色
$t_size  = 4;				# タイトルのサイズ
$t_face  = 'ＭＳ Ｐゴシック';		# タイトル文字のタイプ

$bground = "";				# 壁紙 (パス付きで指定）
$bgcolor = "#CCFFFF";			# 背景色
$text    = "#333333";			# 文字色を指定
$link    = "#663300";			# リンク色を指定（未リンク）
$vlink   = "#330000";			# リンク色を指定（既リンク）
$alink   = "#FF0000";			# リンク色を指定（リンク中）

$pass = '1682';				# 管理用パスワード(英数字)
$home = "http://waiwai.ciao.jp/waiwai/index.shtml";		# 戻り先 (index.htmlなど)
$max  = 100;				# 記事の最大保持数
$pagelog  = 100;				# 表示ファイル第1ページの記事数
$autolink = 1;				# 自動リンク (0=no 1=yes)
$log_dir = ".";				# ログディレクトリ (フルパスだと / から)
$htm_dir = ".";				# 表示ファイルディレクトリ (フルパスだと / から)

# CGIスクリプト自身をURLで指定
$script  = "http://waiwai.ciao.jp/waiwai/sunbbs/ryoma3/sunbbs.cgi";

# 表示ファイル (index.html) のある「ディレクトリ」をURLで指定
$htm_url = "http://waiwai.ciao.jp/waiwai/sunbbs/ryoma3";

## --- 応用設定
$whatsnew = 1;				# 新着情報ボードモード (0=no 1=yes)
$obi_color = "#663300";			# 題名部の色
$point  = '■';				# 題名部ポインタ
$point2 = '▲';				# 戻り先部ポインタ
$p_color = "#CC0000";			# ポインタの色
$s_color = "#FFFFFF";			# 題名の色
$t_gif = "";				# タイトルGIF画像 (http://から記述)
$tg_w = '250';				# タイトル画像の幅
$tg_h = '54';				# タイトル画像の高さ
$date_type = 0;				# 日付の種類 (0=洋式 1=和式)
$logfile = "sunbbs.log";		# ログファイル名
$htmfile = "index.html";		# 表示ファイルHTML(第1ページ)
$nexthtm = "index2.html";		# 表示ファイルHTML(第2ページ)
$tagkey = 0;				# 掲示板使用時のタグ許可 (0=no 1=yes)
$method = 'POST';			# method形式 (POST/GET)
$lockkey = 0;				# ロックファイル処理 (0=no 1=symlink 2=open)
$lockfile = './sunbbs.lock';		# ロックファイル名
$wrap = 'soft';				# 改行形式 (soft=手動 hard=強制)
$nocashe = 1;				# ブラウザのキャッシュ取込を拒否 (0=no 1=yes)
$mailing  = 1;				# 投稿があるとメール通知する(0=no 1=yes)
$mailto = 'waiwai@bi.ciao.jp';		# メールアドレス(メール通知する時)
$sendmail = '/usr/sbin/sendmail';	# sendmailパス（メール通知する時）

## --- 過去ログ設定 (sunbbs2.cgi 必須)
$pastkey = 1;				# 過去ログ機能 (0=no 1=yes) 
$past_dir  = ".";			# 過去ログのあるディレクトリ (フルパスだと / から)
$pastno = './pastno.dat';		# 過去ログカウントファイル
$log_line = '150';			# 過去ログ１ファイル当りの行数の限度
$subfile = './sunbbs2.cgi';		# 補助プログラムのファイル名

## --- 管理者コメント（タイトル下部にちょっとしたコメントを表示できます）
$message = <<"MSG";
宙組／宝塚大劇場2006年11/3～12/12・東京宝塚劇場1/2～2/12
MSG

## --- スタイルシート設定
$ssheet = 1;				# スタイルシートの適用 (0=no 1=yes)
$style = <<"EOM";			# スタイルシートのタグを記述
<STYLE type="text/css">
<!--
a:link    {font-size: 10pt; text-decoration:none; color:$link; }
a:visited {font-size: 10pt; text-decoration:none; color:$vlink; }
a:active  {font-size: 10pt; text-decoration:none; color:$alink; }
a:hover   {font-size: 10pt; text-decoration:underline; color:$alink; }
-->
</STYLE>
EOM

## ----- 設定完了 --------------------- #

# bodyタグを定義
if ($bground) {
   $body = "<body background=\"$bground\" bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink>";
} else {
   $body = "<body bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink>";
}

# HTMLディレクトリ指定で最後に / がついていたら切り捨てる
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

## --- 投稿フォーム１
sub form {
	# パスワードチェック
	if ($whatsnew && $FORM{'pass'} ne "$pass") { &error("パスワードが違います。"); }

	print "Content-type: text/html\n\n";
	print "<html>\n<head><title>$title</title></head>\n";
	print "<frameset rows=\"280\,*\">\n";
	print "<frame name=\"ue\" src=\"$script?mode=form2&pass=$FORM{'pass'}\">\n";
	print "<frame name=\"sita\" src=\"$htm_url/$htmfile#frame\">\n";
	print "<noframes>\n";
	print "$body\n";
	print "<center><font size=4>フレームが利用できないようです。\n";
	print "<P><a href=\"$script?mode=form2&pass=$FORM{'pass'}\">ここをクリック</a> して下さい。\n";
	print "</font></center>\n</body></noframes>\n";
	print "</frameset></html>\n";
	exit;
}

## --- 投稿フォーム２
sub form2 {
	# クッキーを取得
	if ($whatsnew == 1) { &get_cookie; }

	# フォームサイズを定義
	&form_size;

	&header;

	print "<center><form action=\"$script\" method=\"$method\" target=\"main\">\n";
	print "<input type=hidden name=mode value=\"regist\">\n";
	print "<input type=hidden name=pass value=\"$FORM{'pass'}\">\n";

	# 掲示板モードのとき
	if ($whatsnew == 0) {

	  ## -- 返信の場合
	  if ($FORM{'no'}) {
		# ログを開く
		open(DB,"$log_dir/$logfile") || &error("Can't open $logfile");
		@lines = <DB>;
		close(DB);

		# 親記事を検索し分解
		foreach $line (@lines) {
			($num,$date,$name,$email,$sub,$com) = split(/<>/,$line);
			if ($FORM{'no'} eq "$num") {
				if ($sub eq "") { $sub = "no title"; }
				last;
			}
		}

		# 返信用項目を作成
		if ($sub =~ /^Re/) {
			$sub =~ s/Re//;
			$res_sub = "Re\[$num\]" . "$sub";
		} else {
			$res_sub = "Re\[$num\]\: $sub";
		}

		$res_com = "\&gt\; $com";
		$res_com =~ s/<br>/\r\&gt\; /ig;

		print "</center><blockquote>\n";
		print "以下は、記事NO <b>[$num] $sub</b> ($nameさん) に対する返信フォームです。<hr>\n";
		print "【親記事】<P><table width=90% cellpadding=5 border=1><tr>\n";
		print "<td>$com</td></tr></table>\n";
		print "</blockquote><center>\n";
	  }

	  print "<table border=0>\n";
	  print "<tr><td nowrap><b>おなまえ</b></td>\n";
	  print "<td><input type=text name=name size=\"$nam_wid\" value=\"$c_name\"></td></tr>\n";
	  print "<tr><td nowrap><b>Ｅメール</b></td>\n";
	  print "<td><input type=text name=email size=\"$nam_wid\" value=\"$c_email\"></td></tr>\n";

	# 新着ボードモードのとき
	} else {
	  print "投稿する記事を以下のフォームに記述し「投稿する」ボタンを押して下さい。<P>\n";
	  print "<table border=1>\n";
	  print "<tr><td nowrap><b>日　付</b></td>\n";
	  print "<td><input type=text name=date value=\"$date\" size=20></td></tr>\n";
	}

	print "<tr><td nowrap><b>名　前</b></td>\n";
	print "<td><input type=text name=subj size=\"$sub_wid\" value=\"$res_sub\">\n";
	print "<input type=submit value=\"投稿する\">";
	print "<input type=reset value=\"リセット\"></td></tr>\n";
	print "<tr><td colspan=2><b>コメント</b><br>";
	print "<textarea name=comment cols=\"$com_wid\" rows=6 wrap=$wrap>$res_com</textarea></tr>\n";
	print "<tr><td nowrap><b>ＵＲＬ</b></td>";
	print "<td><input type=text name=url size=$url_wid value=\"http://$c_url\"></td></tr>\n";

	if ($whatsnew == 0) {
	  print "<tr><td nowrap><b>削除キー</b></td>";
	  print "<td><input type=password name=pwd size=8 maxlength=8 value=\"$c_pwd\">\n";
	  print "自分の記事を削除時に使用(英数字で8文字以内)</td></tr>\n";
	}

	print "</table></form></center>\n";
	print "</body></html>\n";
	exit;
}

## --- 書込み処理
sub regist {
	# パスワードチェック

	if ($whatsnew && $FORM{'pass'} ne "$pass") { &error("パスワードが違います。"); }

	if ($whatsnew == 0 && $name eq "") { &error("なまえの記入がありません。"); }
	if ($comment eq "") { &error("コメントに記入がありません。"); }

	# ロック開始
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	open(DB,"$log_dir\/$logfile") || &error("Can't open $logfile");
	@lines = <DB>;
	close(DB);

	# 二重投稿の禁止
	($knum,$kdate,$kname,$kemail,$ksubj,$kcom) = split(/<>/,$lines[0]);
	if ($name eq $kname && $comment eq $kcom) { &error("二重投稿は禁止です"); }

	# クッキーを発行
	if ($whatsnew == 1) { &set_cookie; }

	## 過去ログを取得する場合
	if ($pastkey && $#lines >= $max-1) { &pastlog; }

	# 記事Noカウント
	$number = $knum + 1;

	# 最大記事数超を切り捨て
	$i=0;
	@new = ();
	foreach (0 .. $#lines) {
		push (@new,$lines[$i]);
		$i++;
		if ($i >= $max-1) { last; }
	}

	# 削除キーを暗号化
	if ($pwd) { &pwd_encode($pwd); }

	# ホスト名を取得
	&get_host;

	# 日付処理
	if ($whatsnew) { $date = $FORM{'date'}; }

	# ログをフォーマット
	unshift (@new,"$number<>$date<>$name<>$email<>$subj<>$comment<>$url<>$host<>$ango<>\n");
	# ログを更新
	open(DB,">$log_dir\/$logfile") || &error("Can't write $logfile");
	print DB @new;
	close(DB);

	# 全体の記事数を把握
	if ($pagelog < $#new+1) { $flag=1; }

	# HTMLファイルを生成（第１ページ）
	$write_file = "$htm_dir\/$htmfile";
	&html_regist;

	# HTMLファイルを生成（第２ページ）
	if ($flag) {
		$write_file = "$htm_dir\/$nexthtm";
		&html_regist;
	}

	# ロック解除
	unlink($lockfile) if (-e $lockfile);

	# HTMLファイルへ戻る
	&location;

	# メール通知処理
	if ($mailing && $email ne "$mailto") { &mail_to; }

	exit;
}

## --- HTML生成処理
sub html_regist {
	open(HTML,">$write_file") || &error("Can't write $write_file");

	# HTMLヘッダ部
	print HTML "<html>\n<head>\n";
	print HTML "<META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=Shift_JIS\">\n";
	print HTML "<title>$title</title>\n";

	# スタイルシート適用
	if ($ssheet) { print HTML "$style\n"; }

	# キャッシュ取込拒否
	if ($nocashe) { print HTML "<META HTTP-EQUIV=\"Pragma\" CONTENT=\"no-cache\">\n"; }

	print HTML "</head>\n";
	print HTML "$body\n";

	# リンク部
	print HTML "<B><font color=$p_color>$point2</font>";
	print HTML "<a href=\"$home\" target=\"_top\">HomePage</a>\n";

	if ($whatsnew == 0) {
	  print HTML "<font color=$p_color>$point</font>";
	  print HTML "<a href=\"$script?mode=form\">PostMessage</a>\n";
	}

	print HTML "<font color=$p_color>$point</font>";
	print HTML "<a href=\"$script?mode=find\">Search</a>\n";

	# 過去ログ
	if ($pastkey) {
	  print HTML "<font color=$p_color>$point</font>";
	  print HTML "<a href=\"$subfile\">PastLog</a>\n";
	}

	print HTML "<font color=$p_color>$point</font>";
	print HTML "<a href=\"$script?mode=admin_in\">Admin</a>\n";
	print HTML "</B>\n<center>\n<P>\n";

	# タイトル部
	if ($t_gif eq '') {
	  print HTML "<font color=\"$t_color\" size=\"$t_size\" face=\"$t_face\"><b>$title</b></font>\n";
	} else {
	  print HTML "<img src=\"$t_gif\" width=$tg_w height=$tg_h>\n";
	}

	# ひとことメッセージを表示
	$message =~ s/\r\n/<br>/g;
	$message =~ s/\r/<br>/g;
	$message =~ s/\n/<br>/g;

	print HTML "<P>$message</center>\n";
	print HTML "<hr><a name=\"frame\"></a>\n";

	# 記事数を定義
	if ($flag == 2) { $start = $pagelog; $end = $#new; }
	else {
	  $start = 0;
	  if ($i < $pagelog) { $end = $i; }
	  else { $end = $pagelog-1; }
	}

	# 記事を展開
	foreach ($start .. $end) {
	  local($num,$date,$name,$email,$sub,$com,$url,$host) = split(/<>/,$new[$_]);

	  if ($sub eq "") { $sub = "no title"; }
	  if ($autolink) { &auto_link($com); }

	  # 掲示板モードの場合
	  if ($whatsnew == 0) {
		print HTML "<table border=0 width=100% cellpadding=1><tr>\n";
		print HTML "<td bgcolor=$obi_color> <font color=$p_color>$point</font>\n";
		print HTML "<font color=$s_color size=3><b>$sub</b></font></td>\n";
		print HTML "</tr></table>\n";
		print HTML "<table cellspacing=0 cellpadding=0 width=95% align=center>\n";
		print HTML "<tr><td>No.</td><td>：<B>$num</B></td>";
		print HTML "<td></td><td></td></tr>\n";
		print HTML "<tr><td>Name</td><td>：<b>$name</b></td>";
		print HTML "<td></td><td></td></tr>\n";
		print HTML "<tr><td>Date</td><td>：$date</td>";
		print HTML "<td></td><td></td></tr>\n";

		# メール表示
		if ($email) {
		    print HTML "<tr><td>Mail</td><td>：<a href=mailto:$email>$email</a></td>";
		    print HTML "<td></td><td></td></tr>\n";
		}

		# URL表示
		if ($url) {
		    print HTML "<tr><td>URL</td><td>：<a href=http://$url target=_top>http://$url</a></td>";
		    print HTML "<td></td><td></td></tr>\n";
		}

		print HTML "<tr><td></td><td width=100% colspan=3><br>$com</td>\n";
		print HTML "<td align=right valign=bottom>\n";
		print HTML "<form action=\"$script\" method=$method>\n";
		print HTML "<input type=hidden name=mode value=\"form2\">\n";
		print HTML "<input type=hidden name=no value=\"$num\">\n";
		print HTML "<input type=submit value=\"返信\"></form>\n";
		print HTML "</td></tr></table><P>\n";

	  # 新着ボードモードの場合
	  } else {
		print HTML "<table border=0 width=100% cellpadding=2><tr>\n";
		print HTML "<td bgcolor=$obi_color> <font color=$p_color>$point</font>\n";
		print HTML "<font color=$s_color size=3><b>$sub</b></font></td>\n";
		print HTML "</tr></table>\n";
		print HTML "<table><tr><td width=15>　</td>\n";
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

	# 次／前ページのリンクを生成
	if ($flag == 1) {
	  print HTML "<form action=\"$htm_url/$nexthtm\">";
	  print HTML "<input type=submit value=\"次ページ\"></form></td><td>\n";
	  $flag=2;

	} elsif ($flag == 2) {
	  print HTML "<form action=\"$htm_url/$htmfile\">";
	  print HTML "<input type=submit value=\"前ページ\"></form></Td><Td>\n";
	}

	# 削除フォーム
	if ($whatsnew == 0) {
	  print HTML "<form action=\"$script\" method=\"$method\">\n";
	  print HTML "<div align=right><table><tr><td>\n";
	  print HTML "<font color=$t_color>以下のフォームから自分の記事を削除できます</font><br>\n";
	  print HTML "記事No <input type=text name=no size=4>\n";
	  print HTML "削除キー <input type=password name=pwd size=4>\n";
	  print HTML "<input type=hidden name=mode value=\"del\">\n";
	  print HTML "<input type=submit value=\"削除する\"></td></tr></table></div>\n";
	  print HTML "</Td></Tr></Table></form>\n";
	}

	# 著作権を表示（削除禁止）
	print HTML "<center><small><!-- $ver -->\n";
	print HTML "- <a href=\"http://www.kent-web.com/\" target=_top>Sun Board</a> -\n";
	print HTML "</small></center>\n";
	print HTML "</body></html>\n";
	close(HTML);
}

## --- 表示ファイルにジャンプ
sub location {
	# IISサーバ対応
	if ($ENV{PERLXS} eq "PerlIS") {
		print "HTTP/1.0 302 Temporary Redirection\r\n";
		print "Content-type: text/html\n";
	}
	print "Location: $htm_url\/$htmfile\n\n";
}

## --- 管理モード入室画面
sub admin_in {
	&header;
	print "<table width=100%><tr><th bgcolor=$obi_color>\n";
	print "<font color=$s_color>パスワード確認画面</font></th></tr></table>\n";
	print "<P><center><B>パスワードを入力して下さい。</B>\n";
	print "<form action=\"$script\" method=\"$method\">\n";

	# 新着情報ボード時は選択ボタンを表示
	if ($whatsnew) {
		print "<input type=radio name=mode value=\"form\" checked><B>記事書込</B>\n";
	}
	else {
		print "<input type=hidden name=mode value=\"admin\">\n";
	}

	print "<input type=password name=pass size=10>";
	print "<input type=submit value=\" 認証 \"></form>\n";
	print "</center>\n</body>\n</html>\n";
	exit;
}

## --- 管理用初期画面
sub admin {
	# パスワードチェック
	if ($FORM{'pass'} ne "$pass") { &error("パスワードが違います。"); }

	# ログファイルを開く
	open(DB,"$log_dir\/$logfile") || &error("Can't open $logfile");
	@lines = <DB>;
	close(DB);

	&header;
	print "[<a href=\"$htm_url/$htmfile\">掲示板へもどる</a>]\n";
	print "<table width=100%><tr><th bgcolor=$obi_color>\n";
	print "<font color=$s_color>入 力 画 面</font></th></tr></table>\n";

	# 記事編集画面
	if ($FORM{'edit'}) {

	&form_size;

	foreach $line (@lines) {
		($num,$date,$name,$email,$subj,$com,$url,$host) = split(/<>/,$line);
		if ($FORM{'edit'} eq "$num") { last; }
	}

	$com =~ s/<br>/\r/g;
	if ($url) { $url = "http://$url"; }

	print <<"EOM";
<P><center><h4>編集する部分のみ書き換え、編集ボタンを押して下さい。</h4>
<P><form action="$script" method="$method">
<input type=hidden name=pass value="$FORM{'pass'}">
<input type=hidden name=mode value="edit">
<input type=hidden name=edit value="$num">
<table border=0>
EOM
	if ($whatsnew == 0) {
	  print "<tr><td nowrap><b>おなまえ</b></td>";
	  print "<td><input type=text name=name size=$nam_wid value=\"$name\"></td></tr>\n";
	  print "<tr><td nowrap><b>Ｅメール</b></td>";
	  print "<td><input type=text name=email size=$nam_wid value=\"$email\"></td></tr>\n";
	}

	print "<tr><td nowrap><b>タイトル</b></td>";
	print "<td><input type=text name=subj size=\"$sub_wid\" value=\"$subj\"></td></tr>\n";
	print "<tr><td colspan=2><b>コメント</b><br>";
	print "<textarea name=comment cols=$com_wid rows=6 wrap=$wrap>$com</textarea></tr>\n";
	print "<tr><td nowrap><b>ＵＲＬ</b></td>";
	print "<td><input type=text name=url size=\"$url_wid\" value=\"$url\"></td></tr>\n";
	print "<tr><th colspan=2>\n";
	print "<input type=submit value=\"記事を編集する\">";
	print "<input type=reset value=\"リセット\"></th></tr></table>\n";
	}

	# 管理用初期画面
	else {

		print <<"EOM";
<P><center>
<table><tr><td>
  <UL>
  <LI>記事を削除する場合はチェックボックスにチェックを入れ、削除ボタンを押して下さい。
  <LI>記事を編集する場合は、<B>No.</B> をクリックすると編集画面となります。
  </UL>
</td></tr></table>
<P><form action="$script" method="$method">
<input type=hidden name=pass value="$FORM{'pass'}">
<input type=hidden name=mode value="admin_del">
<input type=submit value="記事を削除する"><input type=reset value="リセット"><P>
<table border=1>
<tr><th>削除</th><th>日時</th><th>No.</th><th>タイトル</th>
EOM

	if ($whatsnew == 0) {
		print "<th>なまえ</th><th>ホスト</th>";
	}

	print "<th>コメント</th></tr>\n";

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

## --- 記事削除／編集処理
sub edit {
	# パスワードチェック
	if ($FORM{'pass'} ne "$pass") { &error("パスワードが違います。"); }

	# ロック開始
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	# ログファイルを開く
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
		# 該当記事を抜き出して差し替え
		@new = ();
		foreach $line (@lines) {
		  ($num,$date,$name,$email,$subj,$com,$url,$host,$pwd) = split(/<>/,$line);
		  if ($FORM{'edit'} ne "$num") { push(@new,$line); }
		  else { push(@new,"$num<>$date<>$FORM{'name'}<>$FORM{'email'}<>$FORM{'subj'}<>$comment<>$FORM{'url'}<>$host<>$pwd<>\n"); }
		}
	}

	# ログファイルを上書き
	open(DB,">$log_dir\/$logfile") || &error("Can't write $logfile");
	print DB @new;
	close(DB);

	# 全体の記事数を把握
	if ($pagelog < $#new+1) { $flag=1; }

	# HTMLファイルを生成（第１ページ）
	$i = $#new;
	$write_file = "$htm_dir\/$htmfile";
	&html_regist;

	# HTMLファイルを生成（第２ページ）
	if ($flag) { $write_file = "$htm_dir\/$nexthtm"; &html_regist; }

	# ロック解除
	unlink($lockfile) if (-e $lockfile);

	# 削除処理後は管理画面に戻る
	if ($mode eq "admin_del") { &admin; }

	# 編集処理後は掲示板へ戻る
	else {
		# 表示ファイルに戻る
		&location;
		exit;
	}
}

## --- 記事削除処理
sub msg_del {
	# フォームチェック
	if ($FORM{'no'} eq "") { &error("記事NOが入力されていません。"); }
	if ($FORM{'pwd'} eq "") { &error("削除キーが入力されていません。"); }

	# ロック開始
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	# ログファイルを開く
	open(DB,"$log_dir\/$logfile") || &error("Can't open $logfile");
	@lines = <DB>;
	close(DB);

	# ログを分解し、削除記事を検索
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
	if ($hit == 0) { &error("該当の記事NOが見当たりません。"); }
	if ($delkey eq '') { &error("削除キーが設定されていません。"); }

	# 削除キー照合処理
	$del_flag = 0;
	if ($pwd eq "$pass") { $del_flag = 1; }
	else {
		&pwd_decode($delkey);
		if ($check eq 'yes') { $del_flag = 1; }
	}

	if ($del_flag == 0) { &error("削除キーが違います。"); }

	# ログを更新
	open(DB,">$log_dir\/$logfile") || &error("Can't write $logfile");
	print DB @new;
	close(DB);

	# 全体の記事数を把握
	if ($pagelog < $#new+1) { $flag=1; }

	# HTMLファイルを生成（第１ページ）
	$i = $#new;
	$write_file = "$htm_dir\/$htmfile";
	&html_regist;

	# HTMLファイルを生成（第２ページ）
	if ($flag) { $write_file = "$htm_dir\/$nexthtm"; &html_regist; }

	# ロック解除
	unlink($lockfile) if (-e $lockfile);

	# 初期画面に戻る
	&location;
	exit;
}

## --- フォームからのデータ処理
sub form_decode {
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		if ($ENV{'CONTENT_LENGTH'} > 51200) { &error("投稿量が大きすぎます。"); }
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }

	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

		# 文字コード変換
		&jcode'convert(*value,'sjis');

		# タグ処理
		if ($whatsnew == 0 && $tagkey == 0) {
			$value =~ s/&/&amp\;/g;
			$value =~ s/</&lt\;/g;
			$value =~ s/>/&gt\;/g;
		} else {
			$value =~ s/<!--(.|\n)*-->//g;
			$value =~ s/<>/&lt\;&gt\;/g;
		}

		# 削除処理
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

	# 日時の取得
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
	$year += 1900;
	$mon++;
	if ($mon  < 10) { $mon  = "0$mon";  }
	if ($mday < 10) { $mday = "0$mday"; }
	if ($hour < 10) { $hour = "0$hour"; }
	if ($min  < 10) { $min  = "0$min";  }

	# 日時のフォーマット
	if ($date_type) {
		$youbi = ('日','月','火','水','木','金','土') [$wday];
		if ($whatsnew) {
			$date = "$year年$mon月$mday日 ($youbi)";
		} else {
			$date = "$year年$mon月$mday日 ($youbi) $hour時$min分";
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

## --- エラー処理
sub error {
	unlink($lockfile) if (-e $lockfile);

	&header;
	print "<center><hr width=75%><h3>ERROR !</h3>\n";
	print "<P><font color=$t_color><B>$_[0]</B></font>\n";
	print "<P><hr width=75%></center>\n";
	print "</body></html>\n";
	exit;
}

## --- クッキーの発行
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

## --- クッキーを取得
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

## --- ワード検索サブルーチン
sub find {
	&header;

	print <<"HTML";
[<a href="$htm_url/$htmfile">掲示板にもどる</a>]
<table width=100%>
<tr>
  <th bgcolor="$obi_color">
    <font color="$s_color">ワード検索</font>
  </th>
</tr>
</table>
<P><center>
<table>
<tr>
  <td>
    ■検索したい<b>キーワード</b>を入力し、検索条件を選択し「検索する」を押してください。<br>
    ■複数のキーワードを入力するときは、<b>半角スペース</b>で区切って下さい。
  </td>
</tr>
</table>
<P><form action="$script" method="$method">
<input type=hidden name=mode value="find">
<table border=1>
<tr>
  <th colspan=2>キーワード <input type=text name=word size=30></th>
</tr>
<tr>
  <td>検索条件</td>
  <td>
    <input type=radio name=cond value="and" checked>AND
    <input type=radio name=cond value="or">OR
  </td>
</tr>
<tr>
  <th colspan=2>
    <input type=submit value="検索する"><input type=reset value="リセット">
  </th>
</tr>
</table>
</form></center>
HTML
	# ワード検索の実行と結果表示
	if ($FORM{'word'} ne "") {

		# 入力内容を整理
		$cond = $FORM{'cond'};
		$word = $FORM{'word'};
		$word =~ s/　/ /g;
		$word =~ s/\t/ /g;
		@pairs = split(/ /,$word);

		# ファイルを読み込み
		open(DB,"$log_dir/$logfile") || &error("Can't open $logfile");
		@lines = <DB>;
		close(DB);

		# 検索処理
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

		# 検索終了
		$count = @new;
		print "<hr><b><font color=$t_color>検索結果：$count件</font></b><P>\n";
		print "<OL>\n";

		foreach $line (@new) {
		  ($no,$date,$name,$email,$sub,$com,$url) = split(/<>/,$line);
		  if (!$sub) { $sub = "無題"; }
		  if ($email) { $name = "<a href=mailto:$email>$name</a>"; }
		  if ($url) { $url = "<a href=http://$url target=_top>http://$url</a>"; }

		  # 結果を表示
		  print "<LI>[$no] <font color=$t_color><b>$sub</b></font>\n";
		  print "投稿者：<b>$name</b> <small>投稿日：$date</small>\n";
		  print "<P><blockquote>$com<P>$url</blockquote><hr>\n";
		}

		print "</OL>\n";
	}
	print "</body></html>\n";
	exit;
}

## --- ブラウザを判断しフォーム幅を調整
sub form_size {
	# ブラウザ情報を取得
	$agent = $ENV{'HTTP_USER_AGENT'};

	# MSIE 3 の場合
	if ($agent =~ /MSIE 3/i) {
		$nam_wid = 30;
		$sub_wid = 40;
		$com_wid = 65;
		$url_wid = 48;
	}
	# MSIE 4/5 の場合
	elsif ($agent =~ /MSIE 4/i || $agent =~ /MSIE 5/i) {
		$nam_wid = 30;
		$sub_wid = 40;
		$com_wid = 65;
		$url_wid = 78;
	}
	# その他
	else {
		$nam_wid = 20;
		$sub_wid = 25;
		$com_wid = 56;
		$url_wid = 50;
	}
}

## --- HTMLのヘッダー
sub header { 
	print "Content-type: text/html\n\n";
	print "<html>\n<head>\n";

	# スタイルシート
	if ($ssheet) { print "$style\n"; }

	# キャッシュ取込拒否
	if ($nocashe) { print "<META HTTP-EQUIV=\"Pragma\" CONTENT=\"no-cache\">\n"; }

	print "<META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=x-sjis\">\n";
	print "<title>$title</title></head>\n";
	print "$body\n";
}

## --- パスワード暗号処理
sub pwd_encode {
	$now = time;
	($p1, $p2) = unpack("C2", $now);
	$wk = $now / (60*60*24*7) + $p1 + $p2 - 8;
	@saltset = ('a'..'z','A'..'Z','0'..'9','.','/');
	$nsalt = $saltset[$wk % 64] . $saltset[$now % 64];
	$ango = crypt($_[0], $nsalt);
}

## --- パスワード照合処理
sub pwd_decode {
	if ($_[0] =~ /^\$1\$/) { $crptkey = 3; } # FreeBSDサーバ対応
	else { $crptkey = 0; }
	$check = "no";
	if (crypt($FORM{'pwd'}, substr($_[0],$crptkey,2)) eq "$_[0]") {
		$check = "yes";
	}
}

## --- ロックファイル（symlink関数）
sub lock1 { 
	local($retry) = 5;
	while (!symlink(".", $lockfile)) {
		if (--$retry <= 0) { &error("LOCK is BUSY"); }
		sleep(1);
	}
}

## --- ロックファイル（open関数）
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

## --- ホスト名を取得
sub get_host {
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq "" || $host eq "$addr") {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
	}
	if ($host eq "") { $host = $addr; }
}

## --- 自動リンク
sub auto_link {
	$_[0] =~ s/([^=^\"]|^)(http\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#]+)/$1<a href=$2 target=_top>$2<\/a>/g;
}

## --- メール送信
sub mail_to {
	# 送信内容を JISコード変換
    	&jcode'convert(*title,'jis');
    	&jcode'convert(*name,'jis');
    	&jcode'convert(*subj,'jis');
    	&jcode'convert(*comment,'jis');
	if ($date_type == 1) { &jcode'convert(*date,'jis'); }

	# コメント本文の改行を復元
	$comment =~ s/<br>/\n/ig;
	$comment =~ s/&lt;/</g;
	$comment =~ s/&gt;/>/g;

	# sendmail起動
	if (open(MAIL,"| $sendmail $mailto")) {
	print MAIL "To: $mailto\n";

	# メールアドレスがない場合はダミーメールに置き換え
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

## --- 過去ログ生成
sub pastlog {
	$new_flag = 0;

	open(NUM,"$pastno") || &error("Can't open $pastno");
	$count = <NUM>;
	close(NUM);

	# 過去ログのファイル名を定義
	$pastfile  = "$past_dir\/$count\.html";

	# 過去ログがない場合、新規に自動生成する
	unless(-e $pastfile) { &new_log; }

	if ($new_flag == 0) {
		open (DB,"$pastfile") || &error("Can't open $pastfile");
		@past = <DB>;
		close(DB);
	}

	# 規定の行数をオーバーすると、次ファイルを自動生成する
	if ($#past > $log_line) { &next_log; }

	$pst_line = $lines[$max-1];
	$pst_line =~ s/\n//g;

	($pnum,$pdate,$pname,$pemail,$psub,$pcom,$purl,$phost) = split(/<>/, $pst_line);
	if (!$psub) { $psub = "無題"; }
	if ($pemail) { $pname = "<a href=\"mailto\:$pemail\">$pname</a>"; }
	if ($purl) { $purl = "<a href=http://$purl target=_top>http://$purl</a>"; }

	# 自動リンク
	if ($autolink) { &auto_link($pcom); }

	# 記事のレイアウト
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

}## --- 過去ログ完了 --- ##

## --- 過去ログ次ファイル生成ルーチン
sub next_log {
	# 次ファイルのためのカウントアップ
	$count++;

	# カウントファイル更新
	open(NUM,">$pastno") || &error("Can't write $pastno");
	print NUM "$count";
	close(NUM);

	$pastfile  = "$past_dir\/$count\.html";

	&new_log;
}

## --- 新規過去ログファイル生成ルーチン
sub new_log {
	$new_flag = 1;

	$past[0] = "<html><head><title>過去ログ</title></head>\n";
	$past[1] = "<body background=\"$bground\" bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink><hr size=2>\n";
	$past[2] = "<\!--HAJIME-->\n";
	$past[3] = "<\!--OWARI-->\n";
	$past[4] = "</body></html>\n";

	# 新規過去ログファイルを生成更新
	open(DB,">$pastfile") || &error("Can't write $pastfile");
	print DB @past;
	close(DB);

	# パーミッションを666へ。
	chmod(0666,"$pastfile");
}
