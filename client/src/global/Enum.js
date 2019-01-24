export default class Enum {
    constructor() {
        this.valueIndex = [];
        this.aliasIndex = {};
        this.textIndex = {};

        for (var i = 0; i < arguments.length; i++) {
            var element = arguments[i];
            if (element.value == null) {
                element.value = i;
            }
            this.addElement(element);
        }
    }

    /**
     * 为当前枚举对象添加一个{@link meta.EnumItem 枚举项}
     *
     * @param {meta.EnumItem} element 待添加的枚举项
     * @throws {Error} 如果`value`或`alias`存在重复则抛出异常
     */
    addElement(element) {
        if (this.hasOwnProperty(element.value)) {
            throw new Error('Already defined an element with value' + element.value + ' in this enum type');
        }

        if (this.hasOwnProperty(element.alias)) {
            throw new Error('Already defined an element with alias "' + element.alias + '" in this enum type');
        }

        this[element.value] = element.alias;
        this[element.alias] = element.value;

        this.valueIndex[element.value] = element;
        this.aliasIndex[element.alias] = element;
        this.textIndex[element.text] = element;
    }

    /**
     * 根据数值获取枚举项
     *
     * @param {number} value 数值
     * @return {meta.EnumItem} 对应的枚举项
     */
    fromValue(value) {
        return this.valueIndex[value];
    }

    /**
     * 根据别名获取枚举项
     *
     * @param {string} alias 别名
     * @return {meta.EnumItem} 对应的枚举项
     */
    fromAlias(alias) {
        return this.aliasIndex[alias];
    }

    /**
     * 根据文字获取枚举项
     *
     * @param {string} text 文字
     * @return {meta.EnumItem} 对应的枚举项
     */
    fromText(text) {
        return this.textIndex[text];
    }

    /**
     * 根据数值获取对应枚举项的文字
     *
     * @param {number} value 数值
     * @return {string} 对应的文字
     */
    getTextFromValue(value) {
        return this.fromValue(value).text;
    };

    /**
     * 根据文字获取对应枚举项的文字
     *
     * @param {string} alias 文字
     * @return {string} 对应的文字
     */
    getTextFromAlias(alias) {
        return this.fromAlias(alias).text;
    };

    /**
     * 根据数值获取对应枚举项的数值
     *
     * @param {string} alias 数值
     * @return {number} 对应的数值
     */
    getValueFromAlias(alias) {
        return this.fromAlias(alias).value;
    };

    /**
     * 根据文字获取对应枚举项的数值
     *
     * @param {string} text 文字
     * @return {number} 对应的数值
     */
    getValueFromText(text) {
        return this.fromText(text).value;
    };

    /**
     * 根据数值获取对应枚举项的别名
     *
     * @param {number} value 数值
     * @return {string} 对应的别名
     */
    getAliasFromValue(value) {
        return this.fromValue(value).alias;
    };

    /**
     * 根据文字获取对应枚举项的别名
     *
     * @param {string} text 文字
     * @return {string} 对应的别名
     */
    getAliasFromText(text) {
        return this.fromText(text).alias;
    };

    /**
     * 将当前枚举转换为数组，常用于下拉选择控件之类的数据源
     * 修复原 `{@link Enum.toArray}` 空参时不能正确读取 value 数组的问题
     *
     * @param {...*} args 用于生成数组的提示信息，数组中的每一项可以为字符串或者对象，
     * 为字符串时使用`alias`与字符串相同的{@link meta.EnumItem}对象，为对象时则直接将对象插入到当前位置。
     * 不提供此参数则直接将枚举按`value`属性进行排序生成数组返回
     * @return {meta.EnumItem[]} 每次返回一个全新的数组副本
     * @override
     */
    toArray(...args) {
        let array = [];
        if (args.length > 0) {
            for (let i = 0, l = args.length; i < l; i++) {
                let hint = args[i];
                if (typeof hint === 'string') {
                    array.push(_.clone(this.fromAlias(hint)));
                } else {
                    array.push(hint);
                }
            }
        } else {
            // 必须做一次复制操作，不能让外部的修改影响枚举结构
            // `valueIndex` 本应该设计为一个Object，此处为Array
            // 减少代码改动，简单处理下
            for (let i in this.valueIndex) {
                // 由于`value`不一定是连续的，所以一定要去除空项
                if (this.valueIndex.hasOwnProperty(i) && this.valueIndex[i]) {
                    array.push(this.valueIndex[i]);
                }
            }
        }

        return array;
    }
}