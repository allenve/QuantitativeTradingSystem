/**
 * @file 时间相关的方法
 *
 * @author yupeng(yupeng12@baidu.com)
 * @created: 2019/01/13
 */



import moment from 'moment';

export default {
    getStartTime(date) {
        return moment(date).format('YYYY-MM-DD 00:00:00');
    },
    getEndTime(date) {
        return moment(date).format('YYYY-MM-DD 23:59:59');
    },
    getMonthFirstDay(d) {
        return moment(d || new Date()).format('YYYY-MM-01');
    },
    getMonthFirstDayTime(d) {
        return moment(d || new Date()).format('YYYY-MM-01 00:00:00');
    },
    timeToUtc(timeStr) {
        return moment(timeStr).utc().format('YYYY-MM-DDTHH:mm:ss') + 'Z';
    },
    toUtcTime(utcTimeStr) {
        return moment(utcTimeStr).utc().format('YYYY-MM-DD HH:mm:ss');
    },
    toTime(utcTimeStr) {
        if(utcTimeStr === '' || !utcTimeStr) {
            return '';
        }
        return utcTimeStr ? moment(utcTimeStr).format('YYYY-MM-DD HH:mm:ss') : '';
    },
    utcToMinute(utcTimeStr) {
        if (null != utcTimeStr) {
            return moment(utcTimeStr).format('YYYY-MM-DD HH:mm');
        }

        return '';
    },
    toDate(utcTimeStr) {
        if(utcTimeStr === '' || !utcTimeStr) {
            return '';
        }
        return moment(utcTimeStr).format('YYYY-MM-DD');
    },
    // 检查是否是UTC格式参数
    checkUTC(utcTime, isEndDate) {
        let utcFormat = /^[0-9]{4}-[0-1]?[0-9]{1}-[0-3]?[0-9]{1}T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$/;
        let dateFormat = /^[0-9]{4}-[0-1]?[0-9]{1}-[0-3]?[0-9]{1}$/;
        if (utcFormat.test(utcTime)) {
            return utcTime;
        }
        else if (dateFormat.test(utcTime)) {
            return moment(utcTime + (isEndDate ? ' 23:59:59' : '')).utc().format('YYYY-MM-DDTHH:mm:ss') + 'Z';
        }

        return null;
    },
    checkTime(time, isEndDate) {
        let timeFormat = /^[0-9]{4}-[0-1]?[0-9]{1}-[0-3]?[0-9]{1}\s([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$/;
        let dateFormat = /^[0-9]{4}-[0-1]?[0-9]{1}-[0-3]?[0-9]{1}$/;
        if (timeFormat.test(time)) {
            return time;
        }
        else if (dateFormat.test(time)) {
            return moment(time + (isEndDate ? ' 23:59:59' : '')).format('YYYY-MM-DD HH:mm:ss');
        }

        return null;
    }
};
