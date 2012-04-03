#! /usr/bin/perl

require "./lib/cgi-lib.pl";

use Time::Local;

################################################################################
#
# Setting Parameters
#
################################################################################

$LOG_BG_COLOR = "lightcyan";

# Reserve Availavle Change Day
# 0:Sun 1:Mon 2:Tue 3:Wed 4:Thu 5:Fri 6:Sat
$RSV_BASE_WDAY = 2;
$CAL_BASE_WDAY = 3;

# Section List¤Îµ­½Ò¤È¹ç¤ï¤»¤ë»ö
$MY_SECTION = "Team A";

$MAIL_DOMAIN = "hoge.com";
$SITE_TOP = "homuhomu";
    
################################################################################
#
# System Parameters
#
################################################################################

$EDITION = 1;
$VERSION = 4;
$LEVEL   = 2;

$SCRIPT       = "em.cgi";
$CONF_DIR     = "./conf/";
$VAR_DIR      = "./var/";

$LOG_FILE     = "rsv_log";
$MCFILE       = "mcf";
$LOCK_FILE    = "lock";
$ZONE_LIST    = "zone_list";
$CHANGE_LOG   = "change_log.txt";

@wday_array = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat");

# Time Zone
$END_OF_DAY = 143;

%zone_hash = (
      0 => "00:00\t00:10",   1 => "00:10\t00:20",   2 => "00:20\t00:30",   3 => "00:30\t00:40",   4 => "00:40\t00:50",   5 => "00:50\t01:00",
      6 => "01:00\t01:10",   7 => "01:10\t01:20",   8 => "01:20\t01:30",   9 => "01:30\t01:40",  10 => "01:40\t01:50",  11 => "01:50\t02:00",
     12 => "02:00\t02:10",  13 => "02:10\t02:20",  14 => "02:20\t02:30",  15 => "02:30\t02:40",  16 => "02:40\t02:50",  17 => "02:50\t03:00",
     18 => "03:00\t03:10",  19 => "03:10\t03:20",  20 => "03:20\t03:30",  21 => "03:30\t03:40",  22 => "03:40\t03:50",  23 => "03:50\t04:00",
     24 => "04:00\t04:10",  25 => "04:10\t04:20",  26 => "04:20\t04:30",  27 => "04:30\t04:40",  28 => "04:40\t04:50",  29 => "04:50\t05:00",
     30 => "05:00\t05:10",  31 => "05:10\t05:20",  32 => "05:20\t05:30",  33 => "05:30\t05:40",  34 => "05:40\t05:50",  35 => "05:50\t06:00",
     36 => "06:00\t06:10",  37 => "06:10\t06:20",  38 => "06:20\t06:30",  39 => "06:30\t06:40",  40 => "06:40\t06:50",  41 => "06:50\t07:00",
     42 => "07:00\t07:10",  43 => "07:10\t07:20",  44 => "07:20\t07:30",  45 => "07:30\t07:40",  46 => "07:40\t07:50",  47 => "07:50\t08:00",
     48 => "08:00\t08:10",  49 => "08:10\t08:20",  50 => "08:20\t08:30",  51 => "08:30\t08:40",  52 => "08:40\t08:50",  53 => "08:50\t09:00",
     54 => "09:00\t09:10",  55 => "09:10\t09:20",  56 => "09:20\t09:30",  57 => "09:30\t09:40",  58 => "09:40\t09:50",  59 => "09:50\t10:00",
     60 => "10:00\t10:10",  61 => "10:10\t10:20",  62 => "10:20\t10:30",  63 => "10:30\t10:40",  64 => "10:40\t10:50",  65 => "10:50\t11:00",
     66 => "11:00\t11:10",  67 => "11:10\t11:20",  68 => "11:20\t11:30",  69 => "11:30\t11:40",  70 => "11:40\t11:50",  71 => "11:50\t12:00",
     72 => "12:00\t12:10",  73 => "12:10\t12:20",  74 => "12:20\t12:30",  75 => "12:30\t12:40",  76 => "12:40\t12:50",  77 => "12:50\t13:00",
     78 => "13:00\t13:10",  79 => "13:10\t13:20",  80 => "13:20\t13:30",  81 => "13:30\t13:40",  82 => "13:40\t13:50",  83 => "13:50\t14:00",
     84 => "14:00\t14:10",  85 => "14:10\t14:20",  86 => "14:20\t14:30",  87 => "14:30\t14:40",  88 => "14:40\t14:50",  89 => "14:50\t15:00",
     90 => "15:00\t15:10",  91 => "15:10\t15:20",  92 => "15:20\t15:30",  93 => "15:30\t15:40",  94 => "15:40\t15:50",  95 => "15:50\t16:00",
     96 => "16:00\t16:10",  97 => "16:10\t16:20",  98 => "16:20\t16:30",  99 => "16:30\t16:40", 100 => "16:40\t16:50", 101 => "16:50\t17:00",
    102 => "17:00\t17:10", 103 => "17:10\t17:20", 104 => "17:20\t17:30", 105 => "17:30\t17:40", 106 => "17:40\t17:50", 107 => "17:50\t18:00",
    108 => "18:00\t18:10", 109 => "18:10\t18:20", 110 => "18:20\t18:30", 111 => "18:30\t18:40", 112 => "18:40\t18:50", 113 => "18:50\t19:00",  
    114 => "19:00\t19:10", 115 => "19:10\t19:20", 116 => "19:20\t19:30", 117 => "19:30\t19:40", 118 => "19:40\t19:50", 119 => "19:50\t20:00",   
    120 => "20:00\t20:10", 121 => "20:10\t20:20", 122 => "20:20\t20:30", 123 => "20:30\t20:40", 124 => "20:40\t20:50", 125 => "20:50\t21:00", 
    126 => "21:00\t21:10", 127 => "21:10\t21:20", 128 => "21:20\t21:30", 129 => "21:30\t21:40", 130 => "21:40\t21:50", 131 => "21:50\t22:00",
    132 => "22:00\t22:10", 133 => "22:10\t22:20", 134 => "22:20\t22:30", 135 => "22:30\t22:40", 136 => "22:40\t22:50", 137 => "22:50\t23:00",
    138 => "23:00\t23:10", 139 => "23:10\t23:20", 140 => "23:20\t23:30", 141 => "23:30\t23:40", 142 => "23:40\t23:50", 143 => "23:50\t24:00" 
    );

# log_format() Mode
$LF_ENCODE = 0;
$LF_DECODE = 1;

# disp_log() File Code
$DISP_LOG      = 0;
$DISP_SORT_LOG = 1;

# make_weekly_list() Control Code
$DAY_LIST  = 0;
$WDAY_LIST = 1;
$YDAY_LIST = 2;

# disp_input_form() Control Code
$POST_FORM = 0;
$EDIT_FORM = 1;
$ADMIN_EDIT_FORM = 2;

# disp_sch_cal() Control Code
$SCH_CAL       = 0;
$SCH_CAL_ADMIN = 1;

# Module Control File
$MCF_ADMIN_PASS   =  0;
#$MCF_LOGIN_ID     = 1;
#$MCF_LOGIN_IP     = 2;
$MCF_TIME_OUT     =  3;
$MCF_TIME_ZONE    =  5;
$MCF_POST_CONTROL =  6;
$MCF_CAL_COLOR    =  7;
$MCF_SCH_DAY      =  8;
$MCF_MACHINE      =  9;
$MCF_SECTION      = 10;

################################################################################
#
# File Open
#
################################################################################


# Module Control File Open
&mcfile_open();
sub mcfile_open {
    open(IN, "$CONF_DIR$MCFILE");
    @mcf = ();
    while (<IN>) {
        s/[\r\n]*$//;
        push @mcf, $_;
    }
    close(IN);
}
    
@post_ctrl_list = split(/,/, $mcf[$MCF_POST_CONTROL]);
@CAL_BG_COLOR   = split(/,/, $mcf[$MCF_CAL_COLOR]);

# Login User List File Open
&lock_file_open();
sub lock_file_open {
    open (IN, "$VAR_DIR$LOCK_FILE");
    @lock = ();
    while (<IN>) {
        s/[\r\n]*$//;
        push @lock, $_;
    }
    close (IN);
}

# Reserve Log File Open
&log_file_open();
sub log_file_open {
    open(IN, "$VAR_DIR$LOG_FILE");
    @log = ();
    %log_hash = ();
    while (<IN>) {
        s/[\r\n]*$//;
        push @log, $_;
        &log_format($LF_DECODE, $_);
        $log_hash{$log_num} = $_;
    }
    close(IN);
}

# Zone File Open
&zone_file_open();
sub zone_file_open {
    open(IN, "$CONF_DIR$ZONE_LIST");
    @time_zone_list = ();
    %time_zone_hash = ();
    while (<IN>) {
        my ($key, $zone, $name, $begin, $end, $valid, $view, $flag, $cmb);
        
        s/[\r\n]*$//;
        ($key, $zone, $name, $begin, $end, $valid, $view, $flag, $cmb) = split(/\t/, $_);
        if ($zone == $mcf[$MCF_TIME_ZONE]) {
            push @time_zone_list, $name;
            $time_zone_hash{$name} = "$begin\t$end\t$valid\t$view\t$flag\t$key\t$cmb";
        }
    }
    close(IN);
}

################################################################################
#
# Main Routine
#
################################################################################


print qq|Content-type: text/html; charset=EUC-JP\n\n|;

$mode =$ARGV[0];

# Get Form Data
&ReadParse(*form);

&disp_page_header();

if ($mode eq "sch") {
    &mode_sch();
}

if ($mode eq "post") {
    &mode_post();
    &disp_log($DISP_LOG, -1);
}

if ($mode eq "edit") {
    &mode_edit();
}

if ($mode eq "del") {
    &mode_del();
    $mode = "";
}

if ($mode eq "admin") {
    &mode_admin();
}

if ($mode eq "change_log") {
    &mode_change_log();
}

if ($mode eq "") {
    my @start_day;
    @start_day = &make_weekly_list($YDAY_LIST, time(), $RSV_BASE_WDAY, 0, 1);
#    &disp_calender_log($start_day[0], 7, @fix_log);
    &disp_calender_log($start_day[0], 8, &rsv_log_to_cal_log($RSV_BASE_WDAY, 0, 8));

    @start_day = &make_weekly_list($YDAY_LIST, time(), $RSV_BASE_WDAY, 8, 1);
    &disp_calender_log($start_day[0], 8, &rsv_log_to_cal_log($RSV_BASE_WDAY, 8, 8));

    &disp_log($DISP_LOG, -1);
}

print qq|</body>\n</html>\n|;


################################################################################
#
# Mode
#
################################################################################


# Schedule
#
sub mode_sch {
    my $i;

    print qq|¿§¤ÎÉÕ¤¤¤Æ¤¤¤ëÆü¤ÏÍ½Ìó¤Ç¤­¤Þ¤»¤ó<br>|;
    print qq|<table border="1" cellspacing="0"><tbody align="center">|;
    print qq|<tr>|;
    for ($i = 0; $i <= 6; $i++) {
        print qq|<th>$wday_array[$i]</th>|;
    }
    print qq|</tr>|;
    for ($i = 0; $i <= 7; $i++) {
        &disp_sch_cal($SCH_CAL, ($i * 7));
    }
    print qq|</tbody></table><br>|;
}


# Post
#
sub mode_post {
    if ($post_ctrl_list[$ftime{"wday"}] eq "1") {
        $section = $form{"section"};
        $section_other = $form{"section_other"};
        $name = $form{"name"};
        $pbx = $form{"pbx"};
        $mail = $form{"mail"};
        $rsv_days = $form{"rsv_days"};
        $machine = $form{"machine"};
        $rsv_time = $form{"rsv_time"};
        $usage = $form{"usage"};
        $edit_num = $form{"edit_log"};
        
        &disp_input_form($POST_FORM);

        # Post Log
        if ($form{"reserve"}) {
            &post_log();
        }
    }
    else {
        print qq|º£½µ¤ÎÍ½Ìó¤ÏÄù¤áÀÚ¤ê¤Þ¤·¤¿<hr><br>|;
    }
}


# Edit Log
#
sub mode_edit {
    $edit_num = $form{"edit_log"};
    &disp_log($DISP_LOG, $edit_num);
    print qq|<hr>|;

    if ($form{"edit_log"}) {
        &log_format($LF_DECODE, $log_hash{$edit_num});
        $rsv_days = $rsv_day;
        &disp_input_form($EDIT_FORM);
    }
    elsif ($form{"edit_post"}) {
        my $code;

        $section = $form{"section"};
        $section_other = $form{"section_other"};
        $name = $form{"name"};
        $pbx = $form{"pbx"};
        $mail = $form{"mail"};
        $rsv_days = $form{"rsv_days"};
        $machine = $form{"machine"};
        $rsv_time = $form{"rsv_time"};
        $usage = $form{"usage"};
        $edit_num = $form{"edit_log"};

        &disp_input_form($EDIT_FORM);
        $del_key = "";
        $code = &post_log();
        if ($code == 0) {
            $edit_num = 0;
            $del_key = $edit_num;
            $del_num = $edit_num;
            &del_log();
            &disp_log($DISP_LOG, -1);
        }
    }
}


# Admin Edit Log
#
sub mode_admin_edit {
    $edit_num = $form{"admin_edit_log"};

    if ($form{"admin_edit_log"}) {
        &disp_log_admin($DISP_LOG, $edit_num);
        print qq|<hr>|;
        &log_format($LF_DECODE, $log_hash{$edit_num});
        $rsv_days = $rsv_day;
        &disp_input_form($ADMIN_EDIT_FORM);
    }
    elsif ($form{"admin_edit_post"}) {
        my $code;

        $section       = $form{"section"};
        $section_other = $form{"section_other"};
        $name          = $form{"name"};
        $pbx           = $form{"pbx"};
        $mail          = $form{"mail"};
        $rsv_days      = $form{"rsv_days"};
        $machine       = $form{"machine"};
        $rsv_time      = $form{"rsv_time"};
        $usage         = $form{"usage"};
        $edit_num      = $form{"edit_post"};

        $code = &post_log();
        if ($code == 0) {
            # Reserve Log File Open
            &log_file_open();

            $del_key = $edit_num;
            $del_num = $edit_num;
            &del_log();

            # Reserve Log File Open
            &log_file_open();
        }
        else {
            &disp_log_admin($DISP_LOG, $edit_num);
            print qq|<hr>|;
            &disp_input_form($ADMIN_EDIT_FORM);
        }            
    }
}


# Delete
#
sub mode_del {
    $del_key = $form{"del_key"};

    # Get URL Arg Data
    $del_num = $ARGV[1];

    # Delete Log
    if ($form{"del_log"}) {
        &del_log();
    }
}


# Administrater
#
sub mode_admin() {
    local ($i, $input_pass, $login_id);

    $input_pass    = $form{"input_pass"};
    $login_id = $ARGV[1];

    if ($login_id ne "") {
        my $rc;
        $rc = &check_login_id($login_id);
        if ($rc == 0) {
            &disp_admin_header();
        }
        else {
            print qq|Login Time Out<br>|;
            &disp_login();
        }
    }
    elsif (($form{"login"}) and ($input_pass eq $mcf[$MCF_ADMIN_PASS])) {
        &get_login_id();
        &disp_admin_header();
    }
    else {
        &disp_login();
    }
}


# Change Log
#
sub mode_change_log {
#    if ($form{"change_log_edit"}) {
#        my $change_log;
#        
#        $change_log = $form{"change_log"};
#        $change_log =~ s/[\r\n]*$/\n/g;
#        &file_write("$VAR_DIR$CHANGE_LOG", $change_log);
#    }
#    
#    print qq|<form method="POST" action="$SCRIPT?change_log">|;
#    print qq|<textarea cols="200" rows="30" name="change_log">|;
    open (IN, "$VAR_DIR$CHANGE_LOG");
    while (<IN>) {
        $_ =~ s/[\r\n]*$//g;
        $_ =~ s/ /&nbsp;/g;
        print qq|$_<br>|;
    }
#    print qq|</textarea><br>|;
#    print qq|<input type="submit" name="change_log_edit" value="Edit">|;
#    print qq|</form>|;
}


################################################################################
#
# Function
#
################################################################################


# Display Page Header
#   no arg
sub disp_page_header {
    print <<EOL;
        <html><title>$SITE_TOP</title>
        <body>
        <table><tbody><tr>
        <th><h2>$SITE_TOP</h2></th>
        <td valign="bottom"><h5>ver <a href="$SCRIPT?change_log">$EDITION.$VERSION.$LEVEL</a></h5></td>
        </tr></tbody></table>
        <table><tbody>
        <tr>
        <td><form method="POST" action="$SCRIPT">
        <input type="submit" name="view" value="View">
        </form></td>
        <td><form method="POST" action="$SCRIPT?sch">
        <input type="submit" name="sch" value="Schedule">
        </form></td>
        <td><form method="POST" action="$SCRIPT?post">
        <input type="submit" name="post" value="Post">
        </form></td>
        <td><form method="POST" action="$SCRIPT?admin">
        <input type="submit" name="admin" value="Admin">
        </form></td>
        </tbody></table>
EOL
}


# Display Post Form
#   arg 0 : control
sub disp_input_form {
    my $ctrl;
    my ($base_utime, @day_list, @wday_list, @yday_list, @chkbox, %chkbox);
    my @list;

    $ctrl = $_[0];
    
    $base_utime = time();
    if ($ctrl eq $ADMIN_EDIT_FORM) {
        @day_list  = &make_weekly_list($DAY_LIST, $base_utime, $RSV_BASE_WDAY, 1, 14);
        @wday_list = &make_weekly_list($WDAY_LIST, $base_utime, $RSV_BASE_WDAY, 1, 14);
        @yday_list = &make_weekly_list($YDAY_LIST, $base_utime, $RSV_BASE_WDAY, 1, 14);
    }
    else {
        @day_list  = &make_weekly_list($DAY_LIST, $base_utime, $RSV_BASE_WDAY, 8, 7);
        @wday_list = &make_weekly_list($WDAY_LIST, $base_utime, $RSV_BASE_WDAY, 8, 7);
        @yday_list = &make_weekly_list($YDAY_LIST, $base_utime, $RSV_BASE_WDAY, 8, 7);
    }

    print qq|Á´¹àÌÜÉ¬¿Ü¹àÌÜ¤Ç¤¹<br>|;
    
    print qq|<table border=0><tbody>|;
    print qq|<tr>|;
    if ($ctrl eq $POST_FORM) {
        print qq|<form method="POST" action="$SCRIPT?post">\n|;
    }
    elsif ($ctrl eq $EDIT_FORM) {
        print qq|<form method="POST" action="$SCRIPT?edit">\n|;
    }
    elsif ($ctrl eq $ADMIN_EDIT_FORM) {
        print qq|<form method="POST" action="$SCRIPT?admin+$login_id">\n|;
    }
    print qq|<th align="right">|;
    print qq|Éô½ð:\n|;
    print qq|</th>|;
    print qq|<td colspan=5>|;
    %chkbox = ();
    %chkbox = &chkbox_hash("\0", $section);
    @list = split(/,/, $mcf[$MCF_SECTION]);
    for ($i = 0; $i <= $#list; $i++) {
        print qq|<input type="radio" name="section" value="$list[$i]" $chkbox{$list[$i]}>|;
        print qq|$list[$i]&nbsp;\n|;
    }
    print qq|<input type="radio" name="section" value="other">Other&nbsp;|;
    print qq|<input type="text" name="section_other" size="10" value="$section_other">\n|;
    print qq|</td>|;
    print qq|</tr>|;

    print qq|<tr>|;
    print qq|<th align="right">|;
    print qq|»áÌ¾:|;
    print qq|</th>|;
    print qq|<td colspan="5">|;
    print qq|<input type="text" name="name" size="10" value="$name">&nbsp;|;
    print qq|<b>ÆâÀþ</b>:<input type="text" name="pbx" size="15" value="$pbx">&nbsp;|;
    if ($mail eq "") { $mail = '@' . $MAIL_DOMAIN; }
    print qq|<b>e-mail:</b><input type="text" name="mail" value="$mail" size="40">\n|;
    print qq|</td>|;
    print qq|</tr>|;

    print qq|<tr><td>&nbsp;</td><td colspan=5>&nbsp;</td></tr>|;
    
    print qq|<tr>|;
    print qq|<th align="right">|;
    print qq|¥Þ¥·¥ó:|;
    print qq|</th>|;
    print qq|<td>|;
    %chkbox = ();
    %chkbox = &chkbox_hash("\0", $machine);
    @list = split(/,/, $mcf[$MCF_MACHINE]);
    for ($i = 0; $i <= $#list; $i++) {
        print qq|<input type="radio" name="machine" value="$list[$i]" $chkbox{$list[$i]}>|;
        print qq|$list[$i]<br>\n|;
    }
    print qq|</td>|;
    print qq|<th align="right">|;
    print qq|»î¸³Æü:|;
    print qq|</th>|;
    print qq|<td>|;
    %chkbox = ();
    %chkbox = &chkbox_hash("\0", $rsv_days);

    @chkbox = split(/\t/, $mcf[$MCF_SCH_DAY]);
    for ($i = 0; $i <= $#chkbox; $i++) {
        my ($day, $chk);
        
        ($day, $chk) = (split(/;/, $chkbox[$i]))[0,1];
        $chkbox{$day} = ($chk == 1) ? "disabled" : "";
    }
    
    for ($i = 0; $i <= $#day_list; $i++) {
        print qq|<input type="checkbox" name="rsv_days" value="$yday_list[$i]" $chkbox{$yday_list[$i]}>|;
        print qq|$day_list[$i]&nbsp;($wday_array[$wday_list[$i]])<br>\n|;
    }
    print qq|</th>|;
    print qq|<th align="right">|;
    print qq|»þ´Ö:|;
    print qq|</th>|;
    print qq|<td>|;
    %chkbox = ();
    %chkbox = &chkbox_hash("\0", $rsv_time);
    for ($i = 0; $i <= $#time_zone_list; $i++) {
        my $zone_valid;
        $zone_valid = (split(/\t/, $time_zone_hash{$time_zone_list[$i]}))[2];
        if($zone_valid == 1) {
            print qq|<input type="checkbox" name="rsv_time" value="$time_zone_list[$i]" $chkbox{$time_zone_list[$i]}>$time_zone_list[$i]&nbsp;<br>|;
        }
    }
    print qq|</td>|;
    print qq|</tr>|;
    
    print qq|<tr>|;
    print qq|<th align="right">|;
    print qq|»î¸³ÆâÍÆ:|;
    print qq|</th>|;
    print qq|<td colspan="5">|;
    print qq|<input type="text" name="usage" size="60" value="$usage">|;
    if ($ctrl eq $POST_FORM) {
        print qq|<input type="submit" name="reserve" value="Åê¹Æ">|;
    }
    elsif ($ctrl eq $EDIT_FORM) {
        print qq|<input type="submit" name="edit" value="ÊÔ½¸">|;
        print qq|<input type="hidden" name="edit_post" value="$log_num">|;
    }
    elsif ($ctrl eq $ADMIN_EDIT_FORM) {
        print qq|<input type="submit" name="admin_edit_post" value="ÊÔ½¸">|;
        print qq|<input type="hidden" name="edit_post" value="$log_num">|;
    }
    print qq|</td></tr></form>|;
    print qq|</tbody></table>|;
    print qq|<br><hr>|;
}


# Convert Reserve Log to Calender Log
#   arg 0 : base wday
#   arg 1 : offset
#   arg 2 : rsv day count
sub rsv_log_to_cal_log {
    my ($base_wday, $disp_cnt, $offset, $base_utime, @day_list, @wday_list, @yday_list, %yday_hash);
    my (@tmp_log, @cal_log);
    my %tmp_hash;

    $base_wday = $_[0];
    $offset = $_[1];
    $disp_cnt = $_[2];
    $base_utime = time();
    @day_list  = &make_weekly_list($DAY_LIST, $base_utime, $base_wday, $offset, $disp_cnt);
    @wday_list = &make_weekly_list($WDAY_LIST, $base_utime, $base_wday, $offset, $disp_cnt);
    @yday_list = &make_weekly_list($YDAY_LIST, $base_utime, $base_wday, $offset, $disp_cnt + 1);
    for ($i = 0; $i <= $disp_cnt; $i++) { $yday_hash{$yday_list[$i]} = $i; }
    @tmp_log = @log;    

    # Mask Log by Disp Date
    @cal_log = ();
    for (@tmp_log) {
        &log_format($LF_DECODE, $_);
        if ($yday_hash{$rsv_day} ne "") {
            push (@cal_log, $_);
        }
    }

    # Sort Data by Section, Name
    @tmp_log = ();
    for (@cal_log) { 
        &log_format($LF_DECODE, $_);
        $_ = $section . $name . ",\0" . &log_format($LF_ENCODE);
        push @tmp_log, $_;
    }
    @cal_log = sort { $a cmp $b } @tmp_log;

    @tmp_log = ();
    for (@cal_log) {
        $_ = (split(/,\0/, $_))[1];
        push @tmp_log, $_;
    }
    @cal_log = @tmp_log;

    # Push Reserve Time Zone in Calender Time Zone
    for (@cal_log) {
        &log_format($LF_DECODE, $_);
        if ($END_OF_DAY < $zone_begin) {
            my $re;

            $rsv_day = $yday_list[$yday_hash{"$rsv_day"} + 1];
            $re = $zone_begin - $END_OF_DAY - 1;
            $zone_begin = $re;
            $re = $zone_end   - $END_OF_DAY - 1;
            $zone_end   = $re;
            $tmp_hash{"$machine\t0\t$section\t$name\t$rsv_day"} = &push_rsv_zone($tmp_hash{"$machine\t0\t$section\t$name\t$rsv_day"});
        }
        elsif ($END_OF_DAY < $zone_end) {
            my ($re, $day);
            
            $re = $zone_end - $END_OF_DAY - 1;
            $zone_end = $END_OF_DAY;
            $tmp_hash{"$machine\t0\t$section\t$name\t$rsv_day"} = &push_rsv_zone($tmp_hash{"$machine\t0\t$section\t$name\t$rsv_day"});

            $day = $yday_list[$yday_hash{"$rsv_day"} + 1];
            $rsv_day = $day;
            $zone_begin = 0;
            $zone_end   = $re;
            $tmp_hash{"$machine\t0\t$section\t$name\t$rsv_day"} = &push_rsv_zone($tmp_hash{"$machine\t0\t$section\t$name\t$rsv_day"});
        }
        else {
            $tmp_hash{"$machine\t0\t$section\t$name\t$rsv_day"} = &push_rsv_zone($tmp_hash{"$machine\t0\t$section\t$name\t$rsv_day"});
        }
    }

    # Calculate Colspan Count
    @cal_log = ();
    foreach $key (sort keys %tmp_hash) {
        @tmp_log = split(/\t/, $tmp_hash{$key});
        $tmp_hash{$key} = "";
        for ($i = 0; $i <= $#tmp_log; $i++) {
            my ($col_span, $color);
            ($zone_begin, $zone_end, $log_num) = split(/,/, $tmp_log[$i]);
            $col_span = $zone_end - $zone_begin + 1;
            if ($log_num == 0) { $color = 0; }
            else { $color = 1; }
            
            $tmp_hash{$key} .= "$col_span,$color,$log_num\t";
        }
        
        push (@cal_log, "$key\t$tmp_hash{$key}");
    } 
    return @cal_log;
}


# Push Reserve Time Zone
#   req.  : log_format() data at global variable
#   arg 0 : push reserve zone data
sub push_rsv_zone {
    my (@tmp_log, @push_list, $shift_data);
    my ($t_begin, $t_end, $t_log);
    
    if ($_[0] eq "") {
        @tmp_log = sprintf("0000,%04d,0", $END_OF_DAY);
    }
    else {
        @tmp_log = split(/\t/, $_[0]);
    }

    @push_list = ();
    for ($i = 0; $i <= $#tmp_log; $i++) {
        ($t_begin, $t_end, $t_log) = split(/,/, $tmp_log[$i]);
        if ($t_end <= $zone_begin) {
            push(@push_list, sprintf("%04d,%04d,$t_log", $t_begin, $t_end));
        }
        elsif ($zone_end <= $t_begin) {
            push(@push_list, sprintf("%04d,%04d,$t_log", $t_begin, $t_end));
        }
        elsif ($zone_begin < $t_begin) {
            if ($zone_end < $t_end) {
                push(@push_list, sprintf("%04d,%04d,$log_num", $zone_begin, $zone_end));
                push(@push_list, sprintf("%04d,%04d,$t_log", ($zone_end + 1), $t_end));
            }
            elsif ($zone_end == $t_end) {
                push(@push_list, sprintf("%04d,%04d,$log_num", $zone_begin, $zone_end));
            }
        }
        elsif ($zone_begin == $t_begin) {
            if ($zone_end < $t_end) {
                push(@push_list, sprintf("%04d,%04d,$log_num", $zone_begin, $zone_end));
                push(@push_list, sprintf("%04d,%04d,$t_log", ($zone_end + 1), $t_end));
            }
            elsif ($zone_end == $t_end) {
                push(@push_list, sprintf("%04d,%04d,$log_num", $zone_begin, $zone_end));
            }
        }
        elsif ($t_begin < $zone_begin) {
            if ($zone_end < $t_end) {
                push(@push_list, sprintf("%04d,%04d,$t_log", $t_begin, ($zone_begin - 1)));
                push(@push_list, sprintf("%04d,%04d,$log_num", $zone_begin, $zone_end));
                push(@push_list, sprintf("%04d,%04d,$t_log", ($zone_end + 1), $t_end));
            }
            elsif ($zone_end == $t_end) {
                push(@push_list, sprintf("%04d,%04d,$t_log", $t_begin, ($zone_begin - 1)));
                push(@push_list, sprintf("%04d,%04d,$log_num", $zone_begin, $zone_end));
            }
            elsif ($t_end < $zone_end) {
                push(@push_list, sprintf("%04d,%04d,$t_log", $t_begin, ($zone_begin - 1)));
            }
        }
    }
    for (@push_list) { $shift_data .= "$_\t"; }

    return $shift_data;
}


# Display Calender Log
#   arg 0 : disp start day
#   arg 1 : disp day count
#   arg 2 : log array
sub disp_calender_log {
    my ($base_utime, $disp_cnt, @cal_log, @tmp_log, @mask_zone);
    my (%base_day, $base_day_ref);
    my (@day_list, @wday_list, %yday_hash);
    my ($machine_hash, $i, %ftime);
    my ($machine_color, $tr_hash);

    $base_day_ref = \%base_day;
    
    $disp_cnt  = $_[1];
    @cal_log = @_;
    splice @cal_log, 0, 2;

    ($base_day{"year"}, $base_day{"mon"}, $base_day{"mday"}) = split(/\//, $_[0]);
    $base_utime = &unix_time($base_day_ref);
    %ftime = &format_time($base_utime);
    @day_list  = &make_weekly_list($DAY_LIST, $base_utime, $ftime{"wday"}, 0, $disp_cnt);
    @wday_list = &make_weekly_list($WDAY_LIST, $base_utime, $ftime{"wday"}, 0, $disp_cnt);
    @yday_list = &make_weekly_list($YDAY_LIST, $base_utime, $ftime{"wday"}, 0, $disp_cnt);
    for ($i = 0; $i <= $#yday_list; $i++) {
        $yday_hash{$yday_list[$i]} = $i;
    }
    
    @tmp_log = sort { $a cmp $b } @cal_log;

    # Mask Log by Disp Date
    @cal_log = ();
    for (@tmp_log) {
        my ($machine, $row_cnt, $section, $name, $date, $date_num, @span_data);
        ($machine, $row_cnt, $section, $name, $date, @span_data) = split(/\t/, $_);
        if ($yday_hash{$date} ne "") {
            push (@cal_log, $_);
        }
    }

    # Mask Display Time Zone
    @mask_zone = ();
    for ($i = 0; $i <= $#time_zone_list; $i++) {
        my ($begin, $end, $valid, $view, $flag, $key, $cmb);
        ($begin, $end, $valid, $view, $flag, $key, $cmb) = split(/\t/, $time_zone_hash{$time_zone_list[$i]});
        if ($flag == 0) {
            if ($END_OF_DAY < $begin) {
                $_ = $begin - $END_OF_DAY - 1;
                $begin = $_;
                $_ = $end - $END_OF_DAY - 1;
                $end = $_;
                push (@mask_zone, sprintf("%03d\t%03d\t$valid\t$view\t$i", $begin, $end));
            }
            elsif ($END_OF_DAY < $end) {
                $_ = $end - $END_OF_DAY - 1;
                $end = $_;
                push (@mask_zone, sprintf("%03d\t%$03d\t$valid\t$view\t$i", $begin, $END_OF_DAY));
                push (@mask_zone, sprintf("000\t%03d\t$valid\t$view\t$i", $end));
            }
            else {
                push (@mask_zone, sprintf("%03d\t%03d\t$valid\t$view\t$i", $begin, $end));
            }
        }
    }

    for ($j = 0; $j <= $#cal_log; $j++) {
        my ($machine, $row_cnt, $section, $name, $date, $date_num, @span_log);
        my (@zone, $zone_num);

        # Expand Span Data
        @zone = ();
        $zone_num = 0;
        ($machine, $row_cnt, $section, $name, $date, @span_data) = split(/\t/, $cal_log[$j]);
        for (@span_data) {
            my ($span, $color, $log_num, $i);
            ($span, $color, $log_num) = split(/,/, $_);
            for ($i = 0; $i < $span; $i++) {
                $zone[$zone_num] = "1,$color,$log_num";
                $zone_num++;
            }
        }

        # Clear Unmasked Data
        for (@mask_zone) {
            my ($begin, $end, $view, $i);
            
            ($begin, $end, $view) = (split(/\t/, $_))[0, 1, 3];
            for ($i = $begin; $i <= $end; $i++) {
                if ($view == 0) {
                    $zone[$i] = 0;
                }
            }
        }

        # Merge Span Data
        @span_data = ();
        $zone_num = 0;
        for ($i = ($#zone -1); $i >= 0; $i--) {
            my ($span0, $color0, $log_num0);
            my ($span1, $color1, $log_num1);
            
            ($span0, $color0, $log_num0) = split(/,/, $zone[$i]);
            ($span1, $color1, $log_num1) = split(/,/, $zone[($i + 1)]);
            if ($span0 == 0) {
                splice (@zone, $i, 1);
            }
            elsif (($color0 eq $color1) and ($log_num0 eq $log_num1)) {
                $span0 = $span1 + 1;
                $zone[$i] = "$span0,$color0,$log_num0";
                splice (@zone, ($i + 1), 1);
            }
        }
        $" = "\t";
        $cal_log[$j] = "$machine\t$row_cnt\t$section\t$name\t$date\t@zone";
    }
    
    # Calculation Rowspan Count 
    %machine_hash = ();
    for (@cal_log) {
        my ($machine, $row_cnt, $section, $name, $date, $date_num, @span_data);

        ($machine, $row_cnt, $section, $name, $date, @span_data) = split(/\t/, $_);
        if ($machine_hash{"$machine"} eq "") {
            $machine_hash{"$machine"} = 1;
            $machine_hash{"$machine$section$name"} = 1;
        }
        else {
            if ($machine_hash{"$machine$section$name"} eq "") {
                $machine_hash{"$machine"}++;
                $machine_hash{"$machine$section$name"} = $machine_hash{"$machine"};
            }
        }
    }

    for($i = 0; $i <= $#cal_log; $i++) {
        my ($machine, $row_cnt, $section, $name, $date, $date_num, @span_data);

        ($machine, $row_cnt, $section, $name, $date, @span_data) = split(/\t/, $cal_log[$i]);
        $row_cnt = $machine_hash{"$machine$section$name"};
        $" = "\t";
        $cal_log[$i] = "$machine\t$row_cnt\t$section\t$name\t$date\t@span_data";
    }

    # Merge Data by Same Machine and Name
    %machine_hash = ();
    $blank_span = 0;
    for (@time_zone_list) {
        my ($begin, $end, $view, $flag);
        
        ($begin, $end, $view, $flag) = (split(/\t/, $time_zone_hash{$_}))[0,1,3,4];
        if (($flag == 0) and ($view == 1)) {
            my $data;
            $data = $blank_span + ($end - $begin + 1);
            $blank_span = $data;
        }
    }
    
    for (@cal_log) {
        my ($machine, $row_cnt, $section, $name, $date, $date_num, @span_data, @days_data);
        my $header;
        
        ($machine, $row_cnt, $section, $name, $date, @span_data) = split(/\t/, $_);
        if ($machine_hash{"$machine\t$row_cnt"} eq "") {
            $machine_hash{"$machine\t$row_cnt"} = "$section\t$name";
            for ($i = 0; $i <= $#day_list; $i++) {
                $machine_hash{"$machine\t$row_cnt"} .= "\0$blank_span,0,0";
            }
        }

        ($header, @days_data) = split(/\0/, $machine_hash{"$machine\t$row_cnt"});
        $" = "\t";
        $days_data[$yday_hash{"$date"}] = "@span_data";
        $machine_hash{"$machine\t$row_cnt"} = "$header";
        for (@days_data) { $machine_hash{"$machine\t$row_cnt"} .= "\0$_"; }
    }

    @cal_log = ();
    foreach $key (sort keys %machine_hash) {
        my ($header, @days_data, $data);
        ($header, @days_data) = split(/\0/, $machine_hash{$key});
        $data = "$key\t$header";
        for (@days_data) { $data .= "\t$_"; }
        push (@cal_log, $data);
    }

    @tmp_log = sort { $a cmp $b } @mask_zone;
    @mask_zone = @tmp_log;

    # Display Calender
    print qq|<table border="1" cellspacing="0">|;
    print qq|<tbody align="center">|;
    print qq|<tr>|;
    print qq|<th rowspan="2">ÁõÃÖÌ¾</th>|;
    for ($i = 0; $i <= ($disp_cnt - 1); $i++) {
        print qq|<th colspan="$blank_span">$day_list[$i]<br>$wday_array[$wday_list[$i]]</th>|;
    }
    print qq|<th rowspan="2">»áÌ¾¡÷Éô½ð</th>|;
    print qq|</tr>|;
    print qq|<tr>|;
    for ($i = 0; $i <= ($disp_cnt - 1); $i++) {
        for (@mask_zone) {
            my ($begin, $end, $view, $zone_num);
            
            ($begin, $end, $view, $zone_num) = (split(/\t/, $_))[0,1,3,4];
            if ($view == 1) {
                my $span;
                
                $span = $end - $begin + 1;
                print qq|<th colspan="$span" nowrap>$time_zone_list[$zone_num]</th>|;
            }
        }
    }
    print qq|</tr>|;

    %machine_hash = ();
    for (@cal_log) {
        my ($machine, $row_cnt);
        
        ($machine, $row_cnt) = (split(/\t/, $_))[0, 1];
        $machine_hash{"$machine"} = "$row_cnt";
    }

    %tr_hash = ();
    $machine_color = "";
    for (@cal_log) {
        my ($machine, $row_cnt, $section, $name, @span_data);
        
        ($machine, $row_cnt, $section, $name, @span_data) = split(/\t/, $_);
        if ($tr_hash{"$machine"} eq "") {
            $tr_hash{"$machine"} = 1;
            $machine_color++;
            print qq|<tr><th rowspan="$machine_hash{"$machine"}" nowrap>$machine</th>|;
        }
        else {
            print qq|<tr>|;
        }
        
        for (@span_data) {
            my ($span_cnt, $bgcolor, $log_num);
            
            ($span_cnt, $bgcolor, $log_num) = split(/,/, $_);
            if ($log_num == 0) {
                $log_num = "&nbsp;";
            }
            
            if ($bgcolor == 0) {
                $bgcolor = "$CAL_BG_COLOR[0]";
            }
            else {
                $bgcolor = "$CAL_BG_COLOR[$machine_color]";
            }
            
            &log_format($LF_DECODE, $log_hash{$log_num});
            print qq|<td colspan="$span_cnt" bgcolor="$bgcolor" nowrap>|;
            if ($log_num != 0) {
                print qq|<font size="2"><b>$log_num:</b>$usage</font>|;
            }
            else {
                print qq|&nbsp;|;
            }
        }
        print qq|<td nowrap>$name¡÷$section</td></tr>|;
    }
    print qq|</tbody></table><br>\n|;
}


# Merge Calender Data by Weekly
#   arg 0 : day count of weekly
#   arg 1 : calender data
sub merge_cal_data {
    my ($weekly_cnt, @cal_data);
    my ($machine, $row_cnt, $section, $name, $date, $date_num, @span_data);
    my ($current_machine, $current_row_cnt, $current_section, $current_name);
    my ($blank_span, $td_data, @td_list);
    my (@days_data, $i0);
    my (@yday_list, %yday_hash);

    $weekly_cnt = ($_[0] - 1);
    @cal_data = @_;
    splice @cal_data, 0, 1;

    $blank_span = ($END_OF_DAY + 1);
    for ($i0 = 0; $i0 <= $weekly_cnt; $i0++) {
        print qq|$yday_list[$i0]<br>|;
        $yday_hash{ $yday_list[$i0] } = $i0;
        $days_data[$i0] = "$blank_span,0,0";
    }
    
    # Push EOL Dummy Data
    push @cal_data, "";

    ($machine, $row_cnt, $section, $name, $date, $date_num, @span_data) = split(/\t/, $cal_data[0]);
    $t_machine = $machine;
    $t_row_cnt = $row_cnt;
    $t_section = $section;
    $t_name = $name;
    for (@cal_data) {
        ($machine, $row_cnt, $section, $name, $date, $date_num, @span_data) = split(/\t/, $_);
        if ("$t_machine$t_row_cnt" ne "$machine$row_cnt"){
            $td_data = "$t_machine\t$t_row_cnt\t$t_section\t$t_name";
            for ($i0 = 0; $i0 <= $weekly_cnt; $i0++) { $td_data .= "\t$days_data[$i0]"; }
            push @td_list, $td_data;

            @days_data = ();
            for ($i0 = 0; $i0 <= $weekly_cnt; $i0++) {
                $days_data[$i0] = "$blank_span,0,0";
            }

            $t_machine = $machine;
            $t_row_cnt = $row_cnt;
            $t_section = $section;
            $t_name = $name;
        }
        print qq|$date>>$yday_hash{$date}>>$days_data[$yday_hash{$date}]<br>|;
        $days_data[$yday_hash{ $date }] = "@span_data";
    }
    return  @td_list;
}


# Make Weekly List
#   arg 0 : control
#   arg 1 : now
#   arg 2 : base week day
#   arg 3 : offset days from base week day
#   arg 4 : output count of day
sub make_weekly_list {
    my ($base_wday, $offset_days, $output_cnt, $now_time, $offset, $i);
    my (%ftime, @list);

    $now_time = $_[1];
    $base_wday = $_[2];
    $offset_days = $_[3];
    $output_cnt = $_[4];
    
    %ftime = &format_time($now_time);
    
    if ($ftime{"wday"} > $base_wday) {
        $offset = - ($ftime{"wday"} - $base_wday);
    }
    elsif ($ftime{"wday"} < $base_wday) {
        $offset = - ((7 - $base_wday) + $ftime{"wday"});
    }
    else {
        $offset = 0;
    }
    $offset += $offset_days;
   
    for ($i = 0; $i <= $output_cnt - 1; $i++) {
        %ftime = &format_time(&shift_day($now_time, $offset + $i));
        if ($_[0] == $DAY_LIST) {
            $list[$i] = sprintf("%02d/%02d", $ftime{"mon"}, $ftime{"mday"});
        }
        elsif ($_[0] == $WDAY_LIST) {
            $list[$i] = $ftime{"wday"};
        }
        elsif ($_[0] == $YDAY_LIST) {
            $list[$i] = sprintf("%04d/%02d/%02d", $ftime{"year"}, $ftime{"mon"}, $ftime{"mday"});
        }
    }

    return @list;
}


# Log Format
#   arg0 : mode
#   arg1 : decode data
sub log_format {
    my ($mode, $tmp);

    $mode = $_[0];
    $tmp = $_[1];
    # Log Data Format (Tab Separated Values)
    if ($mode == $LF_ENCODE) {
        return "$machine\t$rsv_day\t$zone_num\t$key\t$log_num\t$rsv_day_num\t$zone_begin\t$zone_end\t$rsv_time\t$section\t$name\t$pbx\t$mail\t$usage\t$post_time";
    }
    elsif ($mode == $LF_DECODE) {
        chomp $tmp;
        ($machine, $rsv_day, $zone_num, $key, $log_num, $rsv_day_num, $zone_begin, $zone_end, $rsv_time, $section, $name, $pbx, $mail, $usage, $post_time) = split(/\t/, $tmp);
    }
}


# Display Log
#   arg0 : log file code
#   arg1 : edit log number
sub disp_log {
    my (@disp_log_file);
    my ($base_utime, @yday_list, %yday_hash);
    
    $base_utime = time();
    @yday_list = &make_weekly_list($YDAY_LIST, $base_utime, $RSV_BASE_WDAY, 8, 8);
    for ($i = 0; $i <= $#yday_list; $i++) { $yday_hash{$yday_list[$i]} = $i; }
    
    @disp_log_file = ();
    if ($_[0] eq $DISP_LOG) {
        for (@log) {
            &log_format($LF_DECODE, $_);
            if ($yday_hash{$rsv_day} ne "") {
                push (@disp_log_file, $_);
            }
        }
    }
    elsif ($_[0] eq $DISP_SORT_LOG) {
        my $sort_log;
        
        @sort_log = sort { $a cmp $b } @log;
        for (@sort_log) {
            &log_format($LF_DECODE, $_);
            if ($yday_hash{$rsv_day} ne "") {
                push (@disp_log_file, $_);
            }
        }
    }

    if (0 < $_[1]) {
        @disp_log_file = ();
        $disp_log_file[0] = $log_hash{$_[1]};
    }
    
    print qq|<table><tbody>|;
    print qq|<tr>|;
    print qq|<th>ÁõÃÖ</th>|;
    print qq|<th>»î¸³Æü</th>|;
    print qq|<th>»î¸³»þ´Ö</th>|;
    print qq|<th>»î¸³ÆâÍÆ</th>|;
    print qq|<th>Éô½ð</th>|;
    print qq|<th>»áÌ¾</th>|;
    print qq|<th>ÆâÀþ</th>|;
    print qq|<th>ºï½ü</th>\n|;
    print qq|</tr>|;

    $i = 0;
    foreach $data (@disp_log_file) {
        &log_format($LF_DECODE, $data);

        if ($i % 2) {
            $tr_tag_op = "";
        } else {
            $tr_tag_op = "bgcolor=\"$LOG_BG_COLOR\"";
        }

        print qq|<tr $tr_tag_op>|;
        print qq|<td>$machine</td>|;
        print qq|<td>$rsv_day</td>|;
        print qq|<td>$rsv_time</td>|;
        print qq|<td>$usage</td>|;
        print qq|<td>$section</td>|;
        print qq|<td>$name</td>|;
        print qq|<td>$pbx</td>|;
        print qq|<form method="POST" action="$SCRIPT?del+$log_num">\n|;
        print qq|<td><input type="submit" name="del_log" value="$log_num">|;
        print qq|<input type="checkbox" name="del_key" value="$log_num"></td>|;
        print qq|</form>|;
        print qq|</tr>\n|;
        $i++;
    }
    print qq|</tbody></table>|;
}


# Display Log for Admin
#   arg0 : log file code
#   arg1 : edit log number
#   arg2 : disp ydays list
sub disp_log_admin {
    my (@yday_list, %yday_hash, @disp_log_file, $data, $i);

    @yday_list = @_;
    splice @yday_list, 0, 2;
    for ($i = 0; $i <= $#yday_list; $i++) { $yday_hash{$yday_list[$i]} = $i; }
    
    if ($_[0] eq $DISP_LOG) {
        for (@log) {
            &log_format($LF_DECODE, $_);
            if ($yday_hash{$rsv_day} ne "") {
                push (@disp_log_file, $_);
            }
        }
    }
    elsif ($_[0] eq $DISP_SORT_LOG) {
        my $sort_log;
        
        @sort_log = sort { $a cmp $b } @log;
        for (@sort_log) {
            &log_format($LF_DECODE, $_);
            if ($yday_hash{$rsv_day} ne "") {
                push (@disp_log_file, $_);
            }
        }
    }

    if (0 < $_[1]) {
        @disp_log_file = ();
        $disp_log_file[0] = $log_hash{$_[1]};
    }

    print qq|<table><tbody>|;
    print qq|<tr>|;
    print qq|<th>ÁõÃÖ</th>|;
    print qq|<th>»î¸³Æü</th>|;
    print qq|<th>»î¸³»þ´Ö</th>|;
    print qq|<th>»î¸³ÆâÍÆ</th>|;
    print qq|<th>Éô½ð</th>|;
    print qq|<th>»áÌ¾</th>|;
    print qq|<th>ÆâÀþ</th>|;
    print qq|<th>¥á¡¼¥ë</th>|;
    print qq|<th>Åê¹ÆÆü»þ</th>|;
    print qq|<th>ÊÔ½¸</th>\n|;
    print qq|<th>ºï½ü</th>\n|;
    print qq|</tr>|;

    $i = 0;
    foreach $data (@disp_log_file) {
        &log_format($LF_DECODE, $data);

        if ($i % 2) {
            $tr_tag_op = "";
        } else {
            $tr_tag_op = "bgcolor=\"$LOG_BG_COLOR\"";
        }

        print qq|<tr $tr_tag_op>|;
        print qq|<td>$machine</td>|;
        print qq|<td>$rsv_day</td>|;
        print qq|<td>$rsv_time</td>|;
        print qq|<td>$usage</td>|;
        print qq|<td>$section</td>|;
        print qq|<td>$name</td>|;
        print qq|<td>$pbx</td>|;
        print qq|<td>$mail</td>|;
        print qq|<td>$post_time</td>|;
        print qq|<form method="POST" action="$SCRIPT?admin+$login_id">\n|;
        print qq|<td><input type="submit" name="admin_edit_log" value="$log_num"></td>|;
        print qq|</form>|;
        print qq|<form method="POST" action="$SCRIPT?admin+$login_id+$log_num">\n|;
        print qq|<td><input type="submit" name="del_log" value="$log_num">|;
        print qq|<input type="checkbox" name="del_key" value="$log_num"></td>|;
        print qq|</form>|;
        print qq|</tr>\n|;

        $i++;
    }
    print qq|</tbody></table>|;
}


# Post Log
#   arg0 : log data @array
sub post_log {
    my (%ftime, %chkbox);
    my (@rsv_day_list, @rsv_time_list, $i, $j, @tmp);

    # Check Blank Item
    $post_error = "";
    if ($section eq "") { $post_error .= "Éô½ð, "; }
    if ($name eq "") { $post_error .= "»áÌ¾, "; }
    if ($pbx eq "") { $post_error .= "ÆâÀþ, "; }
    if (($mail eq '@jp.fujitsu.com') or ($mail eq "")) { $post_error .= "E-Mail, "; }
    if ($machine eq "") { $post_error .= "¥Þ¥·¥ó, "; }
    if ($rsv_days eq "") { $post_error .= "»î¸³Æü, "; }
    if ($rsv_time eq "") { $post_error .= "»þ´Ö, "; }
    if ($usage eq "") { $post_error .= "»î¸³ÆâÍÆ, "; }

    if ($post_error ne "") {
        chop ($post_error);
        chop ($post_error);
        $post_error .= " ¤òÆþÎÏ¤·¤Æ¤¯¤À¤µ¤¤";
    }

        @rsv_time_list = &SplitParam($rsv_time);
    if ($post_error eq "") {
        # Get Time
        %ftime = &format_time(time());
        $post_time = "$ftime{\"year\"}/$ftime{\"mon\"}/$ftime{\"mday\"} $ftime{\"hour\"}:$ftime{\"min\"}:$ftime{\"sec\"}";

        if (($section eq "other") and ($section_other ne "")){
            $section = $section_other;
        }

        ($key) = (split(/\t/, $log[0]))[3];
        $key++;

        @tmp = &SplitParam($section);
        $section = $tmp[0];
        @tmp = &SplitParam($machine);
        $machine = $tmp[0];
        
        @rsv_day_list = &SplitParam($rsv_days);
        @rsv_time_list = &SplitParam($rsv_time);
        %chkbox = &chkbox_hash("\0", $rsv_time);

        # Reserve Time Zone : All Day Check
        for ($i = 0; $i <= $#rsv_time_list; $i++) {
            if ($rsv_time_list[$i] eq "½ªÆü") {
                @rsv_time_list = ();
                $rsv_time_list[0] = "½ªÆü";
                last;
            }
        }
        
        for ($i = 0; $i <= $#rsv_day_list; $i++) {
            for ($j = 0; $j <= $#rsv_time_list; $j++) {
                ($log_num) = (split(/\t/, $log[0]))[4];
                $log_num++;

                $rsv_day = $rsv_day_list[$i];
                $rsv_day_num = 0; # Reserve

                $zone_num = 0; # Reserve
                ($zone_begin, $zone_end) = (split(/\t/, $time_zone_hash{$rsv_time_list[$j]}))[0,1];
                $rsv_time = $rsv_time_list[$j];
                
                # Insart Submit Value at Top of Log
                unshift @log, &log_format($LF_ENCODE);
            }
        }
        
        # Max Log Count
        # splice @log, 1024;
        &file_write("$VAR_DIR$LOG_FILE", @log);
        &file_write("$CONF_DIR$MCFILE", @mcf);
        return 0;
    }
    else {
        print qq|$post_error<br><hr>|;
        &file_write("$CONF_DIR$MCFILE", @mcf);
        return 1;
    }
}


# Delete Log
#   arg0 : log data @array
sub del_log {
    if ($del_num eq $del_key) {
        for ($i = 0; $i <= $#log; $i++) {
            &log_format($LF_DECODE, $log[$i]);
            if ($log_num eq $del_num) {
                splice @log, $i, 1;
            }
        }
        &file_write("$VAR_DIR$LOG_FILE", @log);
    }
}


# Disp Login
#   no arg
sub disp_login {
    print qq|<form method="POST" action="$SCRIPT?admin">|;
    print qq|<input type="password" name="input_pass" size="10">|;
    print qq|<input type="submit" name="login" value="login">|;
    print qq|</form>|;
}


# Get Admin Login Number
#   no arg
sub get_login_id {
    my ($lock_user, @login_user);
    my ($time, $id, $i);

    $login_time = time();

    $lock_user = $lock[0];
    ($time, $id) = split(/\t/, $lock_user);
    if ($mcf[$MCF_TIME_OUT] < ($login_time - $time)) {
        $lock_user = "";
    }

    splice @lock, 0, 1;
    @login_user = ();
    for ($i = 0; $i <= $#lock; $i++) {
        if (($login_time - $time) <= $mcf[$MCF_TIME_OUT]) {
            push @login_user, $lock[$i];
        }
    }

    @lock = ();
    push @lock, $lock_user;
    push @lock, @login_user;
    
    srand($login_time);
    $login_id = int(rand(999999));

    if ($lock[0] eq "") {
        $lock[0] = "$login_time\t$login_id";
        &file_write("$VAR_DIR$LOCK_FILE", @lock);
    }
    else {
        push @lock, "$login_time\t$login_id";
        &file_write("$VAR_DIR$LOCK_FILE", @lock);
    }
}


# Check Login ID
#   arg 0 : login ID
sub check_login_id {
    my (%id_hash, $login_time,  $time, $id, $i);

    $login_time = time();
    
    %id_hash = ();
    for ($i = 0; $i <= $#lock; $i++) {
        ($time, $id) = split(/\t/, $lock[$i]);
        $id_hash{$id} = "$time\t$i";
    }

    ($time, $i) = split(/\t/, $id_hash{$_[0]});
    if (($login_time - $time) <= $mcf[$MCF_TIME_OUT]) {
        $lock[$i] = "$login_time\t$_[0]";
        &file_write("$VAR_DIR$LOCK_FILE", @lock);
        return 0;
    }
    else {
        splice @lock, $i, 1;
        &file_write("$VAR_DIR$LOCK_FILE", @lock);
        return 1;
    }
}
    

# Display Admin Header
#   no arg
sub disp_admin_header {
    print <<EOL;
        <form method="POST" action="$SCRIPT?admin+$login_id">
        <table><tbody>
        <tr>
        <td><input type="submit" name="admin_rsv"  value="Reserve"></td>
        <td><input type="submit" name="admin_mail" value="Mail"></td>
        <td><input type="submit" name="admin_sch"  value="Schedule"></td>
        <td><input type="submit" name="admin_log"  value="Log"></td>
        <td><input type="submit" name="admin_zone" value="Time Zone"></td>
        <td><input type="submit" name="admin_set"  value="Setting"></td>
        </tbody></table>
        </form>
EOL

    if ($form{"admin_rsv"}) {
        &disp_admin_reserve();
    }
    elsif ($form{"admin_edit_log"}) {
        &mode_admin_edit();
        &disp_admin_reserve();
    }
    elsif ($form{"admin_edit_post"}) {
        &mode_admin_edit();
        &disp_admin_reserve();
    }
    elsif ($form{"del_log"}) {
        $del_key = $form{"del_key"};
        $del_num = $ARGV[2];
        
        &del_log();
        &disp_admin_reserve();
    }

    elsif ($form{"admin_mail"}) {
        &disp_admin_mail();
    }

    elsif ($form{"admin_sch"}) {
        &disp_admin_sch();
    }
    elsif ($form{"sch_set"}) {
        &disp_admin_sch();
    }
    
    elsif ($form{"admin_log"}) {
        &disp_admin_log();
    }
    elsif ($form{"log_data_edit"}) {
        &disp_admin_log();
    }
    
    elsif ($form{"admin_set"}) {
        &disp_admin_setting();
    }
    elsif ($form{"list_set"}) {
        &disp_admin_setting();
    }
    elsif ($form{"change_pass"}) {
        &disp_admin_setting();
    }
    elsif ($form{"set_tout"}) {
        &disp_admin_setting();
    }
    elsif ($form{"post_ctrl_set"}) {
        &disp_admin_setting();
    }
    elsif ($form{"admin_zone"}) {
        &disp_admin_zone();
    }
    elsif ($form{"zone_view_set"}) {
        &disp_admin_zone();
    }
    else {
        &disp_admin_reserve();
    }

}


# Disp Admin Reserve
#   no arg
sub disp_admin_reserve {
    my (@edit_log, @remove_log_list);

    @edit_log = &rsv_log_to_cal_log($CAL_BASE_WDAY, 7, 8);
    
    @start_day = &make_weekly_list($YDAY_LIST, time(), $RSV_BASE_WDAY, 1, 1);
    &disp_calender_log($start_day[0], 8, &rsv_log_to_cal_log($RSV_BASE_WDAY, 0, 8));
    print qq|<hr>|;
    &disp_log_admin($DISP_LOG, -1, &make_weekly_list($YDAY_LIST, time(), $RSV_BASE_WDAY, 1, 8));
}


# Disp Admin Mail
#   no arg
sub disp_admin_mail {
    my (@yday_list, %yday_hash, %mail_to, %mail_to_our);
    my (@mail, @sort, $key, $i);
    
    @yday_list = &make_weekly_list($YDAY_LIST, time(), $RSV_BASE_WDAY, 1, 8);
    for ($i = 0; $i <= $#yday_list; $i++) { $yday_hash{$yday_list[$i]} = $i; }

    @mail_log = ();
    for (@log) {
        &log_format($LF_DECODE, $_);
        if ($yday_hash{$rsv_day} ne "") {
            if ($section eq $MY_SECTION) {
                $mail_to_our{$name} = "$section¡Ë$nameÅÂ<$mail>";
            }
            else {
                $mail_to{$name} = "$section¡Ë$nameÅÂ<$mail>";
            }
        }
    }

    @sort = ();
    foreach $key (sort keys %mail_to) {
        push @sort, $mail_to{$key};
    }
    @mail = sort { $a cmp $b } @sort;

    foreach $key (sort keys %mail_to_our) {
        push @mail, $mail_to_our{$key};
    }

    print qq|Mail Address<br>|;
    print qq|<textarea cols="150" rows="5">|;
    for ($i = 0; $i <= ($#mail - 1); $i++) { print qq|$mail[$i],&nbsp;|; }
    print qq|$mail[$#mail]|;
    print qq|</textarea>|;
    print qq|<br><br>|;

    print qq|Mail Subject<br>|;
    print qq|<textarea cols="150" rows="1">|;
    $yday_list[0] =~ s/....\///;
    $yday_list[($#yday_list - 1)] =~ s/....\///;
    print qq|Í½Ìó($yday_list[0]¡Á$yday_list[($#yday_list - 1)])|;
    print qq|</textarea>|;
    print qq|<br><br>|;

    print qq|Mail Header<br>|;
    print qq|<textarea cols="150" rows="3">|;
    for ($i = 0; $i <= ($#mail - 1); $i++) {
        $mail[$i] =~ s/<.*>//g;
        print qq|$mail[$i],&nbsp;|;
    }
    $mail[$#mail] =~ s/<.*>//g;
    print qq|$mail[$#mail]|;
    print qq|</textarea>|;
    
}


# Display Admin Schedule
#   no arg
sub disp_admin_sch {
    my ($sch_day, $i);

    if ($form{"sch_set"}) {
        my (@chkbox, %sch_day);

        %sch_day = ();
        foreach $key (sort keys %form) {
            if (($key =~ /day....\/..\/../) and ($form{$key} ne "")) {
                $key =~ s/day//g;
                $sch_day{$key} = "$key;0;$form{\"day$key\"}";
            }
        }
        
        @chkbox = split(/\0/, $form{"sch_chk"});
        for (@chkbox) {
            $sch_day{$_} = "$_;1;$form{\"day$_\"}\t";
        }

        $mcf[$MCF_SCH_DAY] = "";
        foreach $key (sort keys %sch_day) {
            $mcf[$MCF_SCH_DAY] .= "$sch_day{$key}\t";
        }
        &file_write("$CONF_DIR$MCFILE", @mcf);
    }
    
    print qq|<form method="POST" action="$SCRIPT?admin+$login_id">|;
    print qq|<table border="1" cellspacing="0"><tbody align="center">|;
    print qq|<tr>|;
    for ($i = 0; $i <= 6; $i++) {
        print qq|<th>$wday_array[$i]</th>|;
    }
    print qq|</tr>|;
    for ($i = 0; $i <= 7; $i++) {
        &disp_sch_cal($SCH_CAL_ADMIN, ($i * 7));
    }
    print qq|</tbody></table><br>|;
    print qq|<input type="submit" name="sch_set" value="Schedule Set">|;
    print qq|</form>|;
}


# Display Schedule Calender
#   arg 0 : ctrl
#   arg 1 : offset day
sub disp_sch_cal {
    my (@yday_list, @day_list, @chkbox, %chkbox, %sch, $i);

    @yday_list = &make_weekly_list($YDAY_LIST, time(), 0, $_[1], 7);
    @day_list = @yday_list;

    @chkbox = split(/\t/, $mcf[$MCF_SCH_DAY]);
    for ($i = 0; $i <= $#chkbox; $i++) {
        my ($day, $chk, $sch);

        ($day, $chk, $sch) = split(/;/, $chkbox[$i]);
        $chkbox{$day} = ($chk == 1) ? "checked" : "";
        $sch{$day}    = "$sch";
    }
    
    print qq|<tr>|;
    for ($i = 0; $i <= 6; $i++) {
        $day_list[$i] =~ s/....\///g;
        if ($_[0] eq $SCH_CAL_ADMIN) {
            print qq|<td nowrap>|;
            print qq|<input type="checkbox" name="sch_chk" value="$yday_list[$i]" $chkbox{$yday_list[$i]}>|;
            print qq|$day_list[$i]<br>|;
            print qq|<input type="text" size="32" name="day$yday_list[$i]" value="$sch{$yday_list[$i]}">|;
            print qq|</td>|;
        }
        else {
            my $tag_td;

            $tag_td = ($chkbox{$yday_list[$i]} eq "checked") ? "<td bgcolor=\"$CAL_BG_COLOR[1]\">" : "<td>";
            $sch{$yday_list[$i]} = ($sch{$yday_list[$i]} eq "") ? "&nbsp;" : "$sch{$yday_list[$i]}";
            print qq|$tag_td|;
            print qq|$day_list[$i]<br>$sch{$yday_list[$i]}|;
            print qq|</td>|;
        }
            
    }
    print qq|</tr>|;
}
    

# Disp Admin Log
#   no arg
sub disp_admin_log {
    my $log_data;
    $log_data = $form{"log_data"};
    $log_data =~ s/[\r\n]*$//g;
    
    if ($form{"log_data_edit"}) {
        &file_write("$VAR_DIR$LOG_FILE", $log_data);
        @log = ();
        @log = split(/\n/, $log_data);
    }

    $" = "\n";
    print qq|<form method="POST" action="$SCRIPT?admin+$login_id">|;
    print qq|<textarea cols="200" rows="30" name="log_data">@log</textarea><br>|;
    print qq|<input type="submit" name="log_data_edit" value="Edit">|;
    print qq|</form>|;
}


# Display Time Zone Setting
#   no arg
sub disp_admin_zone {
    my ($i, %chkbox, $key, $zone, $name, $begin, $end, $valid, $view, $flag, $cmb);
    
    if ($form{"zone_view_set"}) {
        my @zone_list;
        my (@f_key, @f_name, %f_valid, %f_view);
        
        @f_key = split(/\0/, $form{"zone_key"});
        @f_name = split(/\0/,$form{"zone_name"});
        %f_valid = &chkbox_hash("\0", $form{"zone_valid"});
        %f_view  = &chkbox_hash("\0", $form{"zone_view"});
        
        open(IN, "$CONF_DIR$ZONE_LIST");
        @zone_list = ();
        while (<IN>) {
            s/[\r\n]*$//;
            push @zone_list, $_;
        }
        close(IN);

        for (@f_key) {
            ($key, $zone, $name, $begin, $end, $valid, $view, $flag, $cmb) = split(/\t/, $zone_list[$_]);
            $name  = $f_name[$_];
            $valid = ($f_valid{$_} eq "checked") ? 1 : 0;
            $view  = ($f_view{$_}  eq "checked") ? 1 : 0;
            $zone_list[$_] = "$key\t$zone\t$name\t$begin\t$end\t$valid\t$view\t$flag\t$cmb";
        }
        &file_write("$CONF_DIR$ZONE_LIST", @zone_list);
    }

    &zone_file_open();
    
    print qq|<form method="post" action"$SCRIPT?admin+$login_id">|;
    print qq|<table border="1" cellspacing="0"><tbody align="center">|;
    print qq|<tr><th>Num</th><th>Name</th><th>Time</th><th>Valid</th><th>View</th><th>Combination</th>|;
    for ($i = 0; $i <= $#time_zone_list; $i++) {
        my ($b_time, $e_time);

        ($begin, $end, $valid, $view, $flag, $key, $cmb) = split(/\t/, $time_zone_hash{$time_zone_list[$i]});
        $b_time = (split(/\t/, $zone_hash{($begin % ($END_OF_DAY + 1))}))[0];
        $e_time = (split(/\t/, $zone_hash{($end % ($END_OF_DAY + 1))}))[1];
        $valid  =~ s/1/checked/g;
        $view   = ($flag == 1) ? "disabled" : $view;
        $view   =~ s/1/checked/g;
        $cmb    = ($cmb eq "") ? "-" : $cmb;

        print qq|<tr>|;
        print qq|<td>$i<input type="hidden" name="zone_key" value="$key"></td>|;
        print qq|<td><input type="text" size="6"name="zone_name" value="$time_zone_list[$i]"></td>|;
        print qq|<td>$b_time&nbsp;-&nbsp;$e_time</td>|;
        print qq|<td><input type="checkbox" name="zone_valid" value="$key" $valid></td>|;
        print qq|<td><input type="checkbox" name="zone_view" value="$key" $view></td>|;
        print qq|<td>$cmb</td>|;
        print qq|</tr>|;
    }
    print qq|</tbody></table>|;
    print qq|<input type="submit" name="zone_view_set" value="Set">|;
    print qq|</form>|;
}


# Disp Admin Setting
#   no arg
sub disp_admin_setting {
    my (%ftime, @list, $data);
    
    if ($form{"list_set"}) {
        my ($machine_data, $section_data, $color_data);
        
        $machine_data  = $form{"machine_data"};
        $section_data  = $form{"section_data"};
        $color_data    = $form{"color_data"};

        $machine_data =~ s/[\r\n]+/\n/g;
        $machine_data =~ s/\n*$//;
        $machine_data =~ s/\n/,/g;
        $mcf[$MCF_MACHINE] = $machine_data;

        $section_data =~ s/[\r\n]+/\n/g;
        $section_data =~ s/\n*$//;
        $section_data =~ s/\n/,/g;
        $mcf[$MCF_SECTION] = $section_data;

        $color_data =~ s/[\r\n]+/\n/g;
        $color_data =~ s/\n*$//;
        $color_data =~ s/\n/,/g;
        $mcf[$MCF_CAL_COLOR] = $color_data;
    }
    
    if ($form{"change_pass"}) {
        my ($input_pass, $re_input_pass);
        
        $input_pass    = $form{"input_pass"};
        $re_input_pass = $form{"re_input_pass"};

        if (($input_pass ne "") and ($input_pass eq $re_input_pass)) {
            $mcf[$MCF_ADMIN_PASS] = $input_pass;
        }
    }

    if ($form{"set_tout"}) {
        my $tout_min;
        
        $tout_min = $form{"tout_value"};

        $mcf[$MCF_TIME_OUT] = $tout_min * 60;
    }
    
    if ($form{"post_ctrl_set"}) {
        my $post_control;
        
        $post_control  = $form{"post_control"};
        
        @data = &SplitParam($post_control);
        @post_ctrl_list = (0,0,0,0,0,0,0);
        for ($i = 0; $i <= $#data; $i++) {
            $post_ctrl_list[$data[$i]] = "1";
        }
        $mcf[$MCF_POST_CONTROL] = "";
        for ($i = 0; $i <= 6; $i++) {
            $mcf[$MCF_POST_CONTROL] .= ($post_ctrl_list[$i] . ",");
        }
        chop($mcf[$MCF_POST_CONTROL]);
    }
    
    &file_write("$CONF_DIR$MCFILE", @mcf);
    
    print qq|<form method="POST" action="$SCRIPT?admin+$login_id">|;
    print qq|<table><tbody>|;
    print qq|<tr>|;
    print qq|<th>Machine<hr></th>|;
    print qq|<th>Section<hr></th>|;
    print qq|<th>Color List<hr></th>|;
    print qq|</tr>|;

    print qq|<tr align="center">|;
    print qq|<td>¥Þ¥·¥ó¥ê¥¹¥ÈÀßÄê</th>|;
    print qq|<td>Í½ÌóÉô½ðÌ¾ÀßÄê</th>|;
    print qq|<td>¥«¥ì¥ó¥À¡¼ÇØ·Ê¿§</th>|;
    print qq|</tr>|;

    print qq|<tr>|;
    print qq|<td><textarea name="machine_data" cols="20" rows="15" wrap="off">|;
    @list = split(/,/, $mcf[$MCF_MACHINE]);
    for (@list) { print qq|$_\n|; }
    print qq|</textarea></td>|;
    print qq|<td><textarea name="section_data" cols="20" rows="15" wrap="off">|;
    @list = split(/,/, $mcf[$MCF_SECTION]);
    for (@list) { print qq|$_\n|; }
    print qq|</textarea></td>|;
    
    print qq|<td><textarea name="color_data" cols="20" rows="15" wrap="off">|;
    @list = split(/,/, $mcf[$MCF_CAL_COLOR]);
    for (@list) { print qq|$_\n|; }
    print qq|</textarea></td>|;
    print qq|</tr>|;
    print qq|</tbody></table>|;
    
    print qq|<table><tbody>|;
    print qq|<tr>|;
    print qq|<td><input type="submit" name="list_set" value="Set List"></td>|;
    print qq|</tr>|;
    print qq|</tbody></table>|;
    print qq|</form>|;
    print qq|<br>|;
    
    # Change Password / Set Time Out Value
    my $tout_min;
    $tout_min = $mcf[$MCF_TIME_OUT] / 60;
    print qq|<form method="POST" action="$SCRIPT?admin+$login_id">|;
    print qq|<table><tbody>|;
    print qq|<tr>|;
    print qq|<th colspan="3">Password<hr></th>|;
    print qq|<th colspan="2">Login Time Out<hr></th>|;
    print qq|</tr>|;
    print qq|<tr>|;
    print qq|<td>New Password</td><td>:</td>|;
    print qq|<td><input type="password" name="input_pass"></td>|;
    print qq|<td><input tyep="text" name="tout_value" value="$tout_min"></td><td>min</td>|;
    print qq|</tr>|;
    print qq|<tr>|;
    print qq|<td>Re-type</td><td>:</td>|;
    print qq|<td><input type="password" name="re_input_pass"></td>|;
    print qq|</tr>|;
    print qq|<tr align="left">|;
    print qq|<td colspan=3><input type="submit" name="change_pass" value="Change Password"></td>|;
    print qq|<td colspan=2><input type="submit" name="set_tout" value="Set Time Out"></td>|;
    print qq|</tr>|;
    print qq|</tbody></table>|;
    print qq|</form>|;
    
    # Post Invalid Control
    print qq|<form method="POST" action="$SCRIPT?admin+$login_id">|;
    print qq|<table><tbody>|;
    print qq|<tr>|;
    print qq|<th colspan="7">Post Available Control<hr></th>|;
    print qq|</tr>|;
    print qq|<tr align="center">|;
    print qq|<td colspan="7">Åê¹Æµö²Ä (check = Åê¹Æ²Ä)</th>|;
    print qq|</tr>|;
    print qq|<tr>|;
    print qq|<th>Sun</th><th>Mon</th><th>Tue</th>|;
    print qq|<th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th>|;
    print qq|</tr>|;
    print qq|<tr>|;
    for ($i = 0; $i <= 6; $i++) {
        $checked = &checkbox_mark_decode($i, @post_ctrl_list);
        print qq|<td><input type="checkbox" name="post_control" value="$i" $checked></td>|;
    }
    print qq|</tr>|;
    print qq|<tr>|;
    print qq|<td  colspan="7">|;
    print qq|<input type="submit" name="post_ctrl_set" value="Set PAC">|;
    print qq|</td>|;
    print qq|</th>|;
    print qq|</tbody></table>|;
    print qq|</form>|;
    
    print qq|<br><hr><br>|;
}


# Separated Value to Hash
#   arg 0 : separate character
#   arg 1 : list data
sub chkbox_hash {
    my (@data, %hash);
    @data = split(/$_[0]/, $_[1]);
    for (@data) { $hash{$_} = "checked"};
    return %hash;
}


# Checkbox Mark Decode
#   arg0 : decode num of array
#   arg1 : target array
sub checkbox_mark_decode {
    my ($i, @data);
    $i = $_[0];
    @data = @_;
    splice @data, 0, 1;
    
    if ($data[$i] == 1) {
        return "checked";
    }
    else {
        return "";
    }
}


# Get Lock and Write File (add break)
#   arg0 : write file
#   arg1 : write data @array
sub file_write {
    my ($file, @list, $data, $i);

    $file = $_[0];
    @list = @_;
    splice @list, 0, 1;

    $i = 0;
    for ($i = 0; $i <= $#list; $i++) {
        $list[$i] .= "\n";
    }
    
    open(OUT, "+< $file");
    flock(OUT, 2);
    truncate(OUT, 0);
    seek(OUT, 0, 0);
    print OUT @list;
    close(OUT);
}


# Format Time
#   arg0 : time(sec)
sub format_time {
    my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst);
    my (%ftime);
    
    ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime($_[0]);
    $ftime{"sec"}   = sprintf("%02d", $sec);
    $ftime{"min"}   = sprintf("%02d", $min);
    $ftime{"hour"}  = sprintf("%02d", $hour);
    $ftime{"mday"}  = sprintf("%02d", $mday);
    $ftime{"mon"}   = sprintf("%02d", ($mon + 1));
    $ftime{"year"}  = sprintf("%04d", ($year + 1900));
    $ftime{"wday"}  = $wday;
    $ftime{"yday"}  = $yday;
    $ftime{"isdst"} = $isdst;

    return %ftime;
}


# Unix Time
#   arg0 : %ftime(year, mon, mday, hour, min, sec)
sub unix_time {
    my $ftime = shift;
    my $utime;
    
    $utime = timelocal($ftime->{"sec"}, $ftime->{"min"}, $ftime->{"hour"}, $ftime->{"mday"}, $ftime->{"mon"} - 1, $ftime->{"year"} - 1900);

    return $utime;
}


# Shift Day
#   arg0 : base day
#   arg1 : shift day from base day
sub shift_day {
    my ($base_day, $shift_cnt, $shift_day);
    
    ($base_day, $shift_cnt) = @_;
    $shift_day = $base_day + ((60 * 60 * 24) * $shift_cnt);
    return($shift_day);
}

