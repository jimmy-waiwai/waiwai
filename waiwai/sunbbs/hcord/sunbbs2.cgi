#!/usr/bin/perl

## SUN BOARD 補助プログラム
## 過去ログ表示・検索システム
## sunbbs2.cgi (1999/09/05)
## by KENT

## ----- 基本設定 --------------------- #

$script = './sunbbs2.cgi';		# スクリプト名
$nofile = './pastno.dat';		# カウントファイル名
$bbsfile  = './index.html';		# 掲示板への戻り先
$method = 'POST';			# method形式 (POST or GET)
$logfile = './sunbbs.log';		# YY-BOARDログファイル
$past_dir = ".";			# 過去ログのディレクトリ（フルパスだと / から）
$past_url = ".";			# 過去ログのＵＲＬ（フルパスだと http:// から）

$bground = "";				# 壁紙（http://から記述）
$bgcolor = "#000000";			# 背景色
$text    = "#FFFFFF";			# 文字色を指定
$link    = "#FFFFCC";			# リンク色を指定（未リンク）
$vlink   = "#FFFF99";			# リンク色を指定（既リンク）
$alink   = "#FFFFFF";			# リンク色を指定（リンク中）

## ----- 設定完了 --------------------- #

## bodyタグを定義
if ($bground) {
	$body = "<body background=\"$bground\" bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink>";
} else {
	$body = "<body bgcolor=$bgcolor text=$text link=$link vlink=$vlink alink=$alink>";
}

# 過去ログカウントファイルを読み込み
open(NUM,"$nofile") || &error("Can't open $nofile");
$count = <NUM>;
close(NUM);


## -------- メイン処理 --------------------------------- ##

&get_form;
if (!$buffer) { &frame; }
&form_decode;

if ($mode eq 'ue_html') { &ue_html; }
if ($mode eq 'find_html') { &find_html; }
if ($mode eq 'do_find') { &do_find; }
exit;

## --------- 処理完了 ---------------------------------- ##

## 検索処理ルーチン
sub do_find {
	@lines = ();
	foreach (1 .. $count) {
		open(DB,"$past_dir\/$_\.html");
		@new_data = <DB>;
		close(DB);

		push(@lines,@new_data);
	}

	$word =~ s/　/ /g;
	$word =~ s/\t/ /g;
	@pairs = split(/ /,$word);

	# 過去ログファイルを読み込み
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
		# ヒットした行を新規配列(@new)に格納
		if ($flag) { push(@new,$line) ; }
	}

	# 検索結果の配列数を数える
	$count = @new;

	# 該当なしの場合
	if ($count == 0) { &nainai; }

	# 結果を出力
	&header;
	print <<"HTML";
<center><table border=1>
<tr><td>
[<a href="$script?mode=find_html">▲ BACK</a>]</td>
<td nowrap>キーワード <b>$word</b> は <b>$count</b>件見つかりました。
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

## フレーム部
sub frame {
	# 過去ログ用カウントファイルをチェック
	unless (-e $nofile) { &error("Don't exist $nofile"); }

	print "Content-type: text/html\n\n";
	print "<html>\n<head><title>PastLog</title></head>\n";
	print "<frameset rows=\"110,*\" FRAMEBORDER=no BORDER=0>\n";
	print "<frame name=\"ue\" src=\"$script?mode=ue_html\" target=\"sita\">\n";
	print "<frame name=\"sita\" src=\"$past_url\/$count\.html\">\n";
	print "<noframes>\n";
	print "$body\n";
	print "<center><h3>フレームの使用できない方は <a href=\"$script?mode=ue_html\">ここをクリック</a> して下さい。\n";
	print "</center>\n</body></noframes>\n";
	print "</frameset></html>\n";
	exit;
}

## 上フレーム（メニュー部）
sub ue_html {
	&header;
	print <<"HTML";
<a href="$bbsfile" target="main">▲ BBS</a>
<a href="$script?mode=find_html" target="sita">■ Seach</a>
<table width=100%>
<tr><th bgcolor=#0000E8>
<font color=#FFFFFF>Past Log</font>
</th></tr></table>
<hr size=2><center>
[<a href="$past_url\/$count\.html" target="sita"><B>NEW</B></a>]
HTML
	# 過去ログの[リンク]を新規順に表示
	for ($i=$count-1; $i>0; $i--) {
		print "[<a href=\"$past_url\/$i\.html\" target=\"sita\">$i</a>]\n";
	}

	print "</center><hr size=2>\n";
	print "</body></html>\n";
	exit;
}

## フォーム取得
sub get_form {
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }
}

## フォームからのデータ処理
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

## 検索該当なし
sub nainai {
	&header;
	print "<center>見つかりませんでした。<hr>\n";
	print "<b>$word</b></center>\n";
	print "</body></html>\n";
	exit;
}

## 検索初期画面
sub find_html {
	&header;
	print <<"HTML";
<center>
<table border=0 cellpadding=10>
<tr><td nowrap>
<center><B>過去ログ検索</B></center>
<OL>
<LI><b>キーワード</b>から該当記事を検索します。
<LI><b>半角スペース</b>で区切って複数のキーワード指定が可\能\です。
<LI><b>検索条件</b>を選択し「検索する」ボタンを押して下さい。
</OL>
</td></tr></table>
<form action="$script" method="$method">
<input type=hidden name=mode value="do_find">
<table border=1>
<tr><td>キーワード</td><td><input type=text name=word size=30></td></tr>
<tr><td>検索条件</td><td><input type=radio name=cond value="and" checked>AND
<input type=radio name=cond value="or">OR</td></tr>
<tr><th colspan=2><input type=submit value="検索する"></th></tr>
</table>
</form></center>
<hr>
</body></html>
HTML
	exit;
}

## HTMLヘッダー部
sub header {
	print "Content-type: text/html\n\n";
	print "<html>\n<head>\n";
	print "<META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=Shift_JIS\">\n";
	print "<title>編集ファイル</title></head>\n";
	print "$body\n";
}

## エラー処理
sub error {
	&header;
	print "<center><hr width=75%><P><h3>ERROR !</h3>\n";
	print "<P><font color=#dd0000><B>$_[0]</B></font>\n";
	print "<P><hr width=75%></center>\n";
	print "</body></html>\n";
	exit;
}

