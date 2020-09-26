package org.trufflephp.nodes.assign;

import org.trufflephp.nodes.PhpExprNode;

/**
 * @author abertschi
 */
public abstract class AssignSemanticNode extends PhpExprNode {

    /**
     * A value that can be passed around and is either copied or passed by reference
     */
    public abstract Object executeSource(Object source);
}
